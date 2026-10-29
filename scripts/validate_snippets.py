#!/usr/bin/env python3
"""
Validation Script for Softel Chat Agent Espanso Snippets
Kiểm tra tính hợp lệ cú pháp YAML, phát hiện trùng lặp trigger và thống kê phím tắt.
"""

import os
import sys

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

    # Fallback line-by-line parser
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

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    match_dir = os.path.join(base_dir, 'espanso', 'match')

    if not os.path.exists(match_dir):
        print(f"Error: Directory '{match_dir}' not found!")
        sys.exit(1)

    print("=" * 60)
    print("SOFTEL CHAT AGENT - ANTI-GRAVITY SNIPPET AUDIT")
    print("=" * 60)

    all_triggers = {}
    total_files = 0
    total_snippets = 0
    errors = 0

    for filename in sorted(os.listdir(match_dir)):
        if filename.endswith(('.yml', '.yaml')):
            total_files += 1
            filepath = os.path.join(match_dir, filename)
            try:
                matches = parse_yaml_matches(filepath)
                print(f"[*] {filename:26s} : {len(matches):3d} snippets found")
                total_snippets += len(matches)
                for trigger, replace in matches:
                    if trigger in all_triggers:
                        print(f"  [!] DUPLICATE TRIGGER DETECTED: '{trigger}' in {filename} (also in {all_triggers[trigger]})")
                        errors += 1
                    else:
                        all_triggers[trigger] = filename
            except Exception as e:
                print(f"  [X] ERROR reading {filename}: {e}")
                errors += 1

    print("-" * 60)
    print(f"Tổng số file match:     {total_files}")
    print(f"Tổng số phím tắt:       {total_snippets}")
    print(f"Số lỗi / trùng lặp:     {errors}")
    print("=" * 60)

    if errors == 0:
        print(">>> KIỂM TRA THÀNH CÔNG: Toàn bộ phím tắt Anti-Gravity đều chuẩn xác, không bị trùng lặp!")
        return 0
    else:
        print(">>> CẢNH BÁO: Phát hiện lỗi cấu hình cần chỉnh sửa trước khi nạp vào Espanso.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
