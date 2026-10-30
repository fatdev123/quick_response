#!/usr/bin/env python3
"""
Validation Script for Softel Chat Agent Espanso Snippets
Kiểm tra tính hợp lệ cú pháp YAML, phát hiện trùng lặp trigger, bắt lệch thông số SLA (Mục 1),
phát hiện lỗi Fatal QA (Mục 2) và ngăn chặn lộ thông tin nội bộ (Mục 3).
"""

import os
import sys
import re

# Ensure UTF-8 output across all operating systems
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

def parse_yaml_matches(filepath):
    """
    Parses triggers and replacements from YAML file using PyYAML or fallback parser.
    """
    matches = []
    if HAS_YAML:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            if data and isinstance(data, dict) and 'matches' in data:
                for item in data['matches']:
                    if isinstance(item, dict) and 'trigger' in item:
                        content = item.get('replace') or item.get('form') or ''
                        matches.append((item['trigger'], str(content)))
        return matches

    current_trigger = None
    current_replace = []
    in_block = False

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            sline = line.strip()
            if sline.startswith('- trigger:'):
                if current_trigger and current_replace:
                    matches.append((current_trigger, ' '.join(current_replace)))
                raw_trig = sline.replace('- trigger:', '').strip()
                if (raw_trig.startswith('"') and raw_trig.endswith('"')) or (raw_trig.startswith("'") and raw_trig.endswith("'")):
                    current_trigger = raw_trig[1:-1]
                else:
                    current_trigger = raw_trig
                current_replace = []
                in_block = False
            elif sline.startswith('replace:') or sline.startswith('form:'):
                prefix = 'replace:' if sline.startswith('replace:') else 'form:'
                raw_rep = sline.replace(prefix, '').strip()
                if (raw_rep.startswith('"') and raw_rep.endswith('"')) or (raw_rep.startswith("'") and raw_rep.endswith("'")):
                    current_replace.append(raw_rep[1:-1])
                elif raw_rep.startswith('"'):
                    current_replace.append(raw_rep[1:])
                    in_block = True
                elif raw_rep.startswith('|'):
                    in_block = True
                elif raw_rep:
                    current_replace.append(raw_rep)
            elif in_block:
                if sline.endswith('"'):
                    current_replace.append(sline[:-1])
                    in_block = False
                elif not sline.startswith('- trigger:'):
                    current_replace.append(sline)
                else:
                    in_block = False

        if current_trigger and current_replace:
            matches.append((current_trigger, ' '.join(current_replace)))

    return matches

def audit_policy_parameters(trigger, text, filename):
    """
    Mục 1: Bắt lệch thông số SLA, thời hạn, điều kiện giữa các snippet và quy chuẩn chuẩn hóa.
    """
    issues = []
    lower_text = text.lower()

    # 1. Hoàn tiền (Refund): Phải tuân thủ 15d máy cũ, 30d máy mới, 7d hàng không lỗi
    if any(k in trigger for k in ['refund', 'c_refund', 'vi_refund', 'vi_c_refund']):
        if 'blanket 7' in lower_text or ('7 calendar days' in lower_text and '15' not in lower_text and '30' not in lower_text):
            issues.append(f"[Mục 1 Lệch SLA] '{trigger}': Áp dụng sai quy tắc hoàn tiền (thiếu 15 ngày máy cũ / 30 ngày máy mới).")

    # 2. Bảo hành (Warranty): Phải tuân thủ 15d máy cũ, 30d máy mới, 48h nứt vỡ ngoại quan
    if any(k in trigger for k in ['war_ylw', 'c_war', 'vi_war', 'vi_c_war']):
        if 'cosmetic' in lower_text or 'nứt' in lower_text or 'physical' in lower_text:
            if '48' not in lower_text:
                issues.append(f"[Mục 1 Lệch SLA] '{trigger}': Thiếu mốc thời gian báo nứt vỡ ngoại quan 48 giờ.")

    # 3. Port-Out PIN: Bắt buộc đúng 4 ngày (96 giờ), cấm báo 30 ngày
    if any(k in trigger for k in ['po_pin', 'c_po', 'vi_portout_pin', 'vi_c_po']):
        if '30 day' in lower_text or '30 ngày' in lower_text:
            issues.append(f"[Mục 1 Lệch SLA] '{trigger}': Báo sai hạn PIN Port-out (chuẩn là 4 ngày / 96 giờ).")

    # 4. Non-usage Lifeline: 30 ngày cước + 15 ngày cure = 45 ngày; Ngày 46 de-enroll
    if any(k in trigger for k in ['nonuse_rule', 'c_nonuse', 'vi_nonuse_rule']):
        if '30' not in lower_text or ('45' not in lower_text and '15' not in lower_text):
            issues.append(f"[Mục 1 Lệch SLA] '{trigger}': Báo sai chu kỳ Non-usage (chuẩn: 30d cước + 15d cure notice).")

    # 5. Khóa MDM Cam kết: Đúng 180 ngày (cấm báo 365 ngày)
    if any(k in trigger for k in ['mdm_disclosure', 'vi_mdm_disclosure']):
        if '365' in lower_text and '180' not in lower_text:
            issues.append(f"[Mục 1 Lệch SLA] '{trigger}': Khóa MDM phải là 180 ngày hoạt động liên tục.")

    # 6. Mã PUK: Cảnh báo 10 lần nhập sai cháy SIM
    if any(k in trigger for k in ['puk_warning', 'c_puk', 'vi_puk_warning', 'vi_c_puk']):
        if '10' not in lower_text:
            issues.append(f"[Mục 1 Lệch SLA] '{trigger}': Thiếu cảnh báo nhập sai PUK 10 lần hủy SIM vĩnh viễn.")

    # 7. Đổi số MDN: 2 lần miễn phí trong 3 kỳ cước
    if any(k in trigger for k in ['mdn_policy', 'vi_mdn_policy']):
        if '2' not in lower_text or '25' not in lower_text:
            issues.append(f"[Mục 1 Lệch SLA] '{trigger}': Đổi số phải nêu rõ hạn mức 2 lần miễn phí / phí $25.")

    return issues

def audit_qa_and_internal_leaks(trigger, text, filename):
    """
    Mục 2 & Mục 3: Bắt lỗi có thể bị QA phạt (Fatal QA) hoặc làm lộ thông tin nội bộ cho khách hàng.
    """
    issues = []
    lower_text = text.lower()

    # Bỏ qua file ghi chú nội bộ CRM (10_crm_notes.yml)
    if filename == '10_crm_notes.yml':
        return issues

    # 1. Chống lộ từ khóa nhạy cảm / nghiệp vụ ngầm (Mục 3)
    leaked_keywords = ['byod cheat', 'cheat', 'lách luật', 'hết cứu', 'cứu được', 'khangtran', 'hthcomm.com']
    for kw in leaked_keywords:
        if kw in lower_text:
            issues.append(f"[Mục 3 Lộ Nội Bộ] '{trigger}' trong {filename}: Chứa từ khóa nhạy cảm nội bộ '{kw}'.")

    # 2. Chống lỗi Fatal QA: Nhắc cam kết 180 ngày quá sớm (Mục 2 - Slide 138)
    # Quy tắc: Tuyệt đối không nhắc 180-day commitment trong macro chào hỏi / transfer-out thông thường / non-usage
    if any(k in trigger for k in [';r_transfer', ';vi_transfer', ';r_nonusage', ';vi_nonusage']):
        if '180' in lower_text or 'subsidy fee' in lower_text:
            issues.append(f"[Mục 2 Lỗi QA Phạt] '{trigger}' trong {filename}: Nhắc cam kết 180 ngày quá sớm khi chưa có xác nhận hủy/buy-out (Slide 138).")

    # 3. Kiểm tra biến động interactive forms
    placeholders = re.findall(r'\[\[(.*?)\]\]', text)
    for p in placeholders:
        if not p.isidentifier():
            issues.append(f"[Mục 2 Lỗi QA Form] '{trigger}': Tên biến form '[[{p}]]' không hợp lệ.")

    return issues

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    match_dir = os.path.join(base_dir, 'espanso', 'match')

    if not os.path.exists(match_dir):
        print(f"Error: Directory '{match_dir}' not found!")
        sys.exit(1)

    print("=" * 70)
    print("SOFTEL CHAT AGENT - KIỂM TOÁN SNIPPET TOÀN DIỆN (CLEAN ARCHITECTURE)")
    print("Mục 1: Bắt lệch SLA | Mục 2: Bắt lỗi QA phạt | Mục 3: Chống lộ nội bộ")
    print("=" * 70)

    all_triggers = {}
    total_files = 0
    total_snippets = 0
    syntax_errors = 0
    policy_discrepancies = 0
    leak_errors = 0

    for filename in sorted(os.listdir(match_dir)):
        if filename.endswith(('.yml', '.yaml')):
            total_files += 1
            filepath = os.path.join(match_dir, filename)
            try:
                matches = parse_yaml_matches(filepath)
                print(f"[*] {filename:26s} : {len(matches):3d} snippets")
                total_snippets += len(matches)
                for trigger, content in matches:
                    # Kiểm tra trùng lặp phím tắt
                    if trigger in all_triggers:
                        print(f"  [X] TRÙNG LẶP TRIGGER: '{trigger}' tại {filename} (đã có tại {all_triggers[trigger]})")
                        syntax_errors += 1
                    else:
                        all_triggers[trigger] = filename

                    # Kiểm tra Mục 1: Bắt lệch SLA / Thông số
                    p_issues = audit_policy_parameters(trigger, content, filename)
                    for pi in p_issues:
                        print(f"  [!] {pi}")
                        policy_discrepancies += 1

                    # Kiểm tra Mục 2 & 3: Bắt lỗi QA phạt và Lộ thông tin nội bộ
                    l_issues = audit_qa_and_internal_leaks(trigger, content, filename)
                    for li in l_issues:
                        print(f"  [X] {li}")
                        leak_errors += 1

            except Exception as e:
                print(f"  [X] LỖI CÚ PHÁP {filename}: {e}")
                syntax_errors += 1

    print("-" * 70)
    print(f"Tổng số file match:           {total_files}")
    print(f"Tổng số phím tắt:             {total_snippets}")
    print(f"Lỗi trùng lặp / cú pháp:      {syntax_errors}")
    print(f"Lỗi lệch thông số SLA (Mục 1): {policy_discrepancies}")
    print(f"Lỗi QA & Lộ nội bộ (Mục 2, 3): {leak_errors}")
    print("=" * 70)

    total_failures = syntax_errors + policy_discrepancies + leak_errors
    if total_failures == 0:
        print(">>> KIỂM TRA THÀNH CÔNG: Hệ thống đạt chuẩn 100% QA, không lệch SLA, không lộ nội bộ!")
        return 0
    else:
        print(f">>> CẢNH BÁO: Phát hiện {total_failures} điểm cần khắc phục trước khi đưa vào sản xuất.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
