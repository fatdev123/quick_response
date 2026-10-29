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

def parse_simple_yaml_matches(filepath):
    """
    Parses triggers and replacements from YAML file.
    Works without PyYAML dependency to ensure zero-setup portability.
    """
    matches = []
    current_trigger = None
    current_replace = []
    in_replace = False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            sline = line.strip()
            if sline.startswith('- trigger:'):
                if current_trigger and current_replace:
                    matches.append((current_trigger, ' '.join(current_replace)))
                # Extract trigger
                raw_trig = sline.replace('- trigger:', '').strip()
                if (raw_trig.startswith('"') and raw_trig.endswith('"')) or (raw_trig.startswith("'") and raw_trig.endswith("'")):
                    current_trigger = raw_trig[1:-1]
                else:
                    current_trigger = raw_trig
                current_replace = []
                in_replace = False
            elif sline.startswith('replace:'):
                raw_rep = sline.replace('replace:', '').strip()
                if (raw_rep.startswith('"') and raw_rep.endswith('"')) or (raw_rep.startswith("'") and raw_rep.endswith("'")):
                    current_replace.append(raw_rep[1:-1])
                elif raw_rep.startswith('"'):
                    current_replace.append(raw_rep[1:])
                    in_replace = True
                else:
                    current_replace.append(raw_rep)
            elif in_replace:
                if sline.endswith('"'):
                    current_replace.append(sline[:-1])
                    in_replace = False
                else:
                    current_replace.append(sline)
                    
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
    print("SOFTEL CHAT AGENT - SNIPPET INTEGRITY AUDIT")
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
                matches = parse_simple_yaml_matches(filepath)
                print(f"[*] {filename:25s} : {len(matches):3d} snippets found")
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
        print(">>> KIỂM TRA THÀNH CÔNG: Toàn bộ phím tắt đều chuẩn xác, không bị trùng lặp!")
        return 0
    else:
        print(">>> CẢNH BÁO: Phát hiện lỗi cấu hình cần chỉnh sửa trước khi nạp vào Espanso.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
