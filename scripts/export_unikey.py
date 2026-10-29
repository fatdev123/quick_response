#!/usr/bin/env python3
"""
Export Script: Converts Espanso YAML snippets into Unikey/EVKey Macro format (ukmacro.txt)
Giúp Agent sử dụng ngay bảng phím tắt nếu máy công ty không cho cài Espanso.
"""

import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def parse_simple_yaml_matches(filepath):
    matches = []
    current_trigger = None
    current_replace = []
    in_replace = False
    
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
    output_file = os.path.join(base_dir, 'unikey_macro.txt')
    
    if not os.path.exists(match_dir):
        print(f"Error: Directory '{match_dir}' not found!")
        sys.exit(1)
        
    all_macros = []
    
    for filename in sorted(os.listdir(match_dir)):
        if filename.endswith(('.yml', '.yaml')):
            filepath = os.path.join(match_dir, filename)
            matches = parse_simple_yaml_matches(filepath)
            for trigger, replace in matches:
                # Remove leading semicolon for Unikey if desired or keep it
                # Unikey supports characters like ; in trigger
                clean_replace = replace.replace('\n', ' ').strip()
                all_macros.append(f"{trigger}:{clean_replace}")
                
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write("# UNIKEY / EVKEY MACRO TABLE FOR SOFTEL CHAT AGENT\n")
        out.write("# To use: Open Unikey -> Expand (Mở rộng) -> Check 'Enable Macro' (Bật tính năng gõ tắt)\n")
        out.write("# -> Click 'Macro Table' (Bảng gõ tắt) -> Select or paste content from this file.\n")
        out.write("\n".join(all_macros))
        out.write("\n")
        
    print(f"Đã xuất thành công {len(all_macros)} phím tắt sang file: {output_file}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
