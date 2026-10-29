#!/usr/bin/env python3
"""
Export Script: Converts Espanso YAML snippets into Unikey/EVKey Macro format (ukmacro.txt)
Hỗ trợ chuyển đổi toàn bộ kho phím tắt Anti-Gravity sang định dạng Unikey/EVKey.
"""

import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

def parse_yaml_matches(filepath):
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
            elif sline.startswith('replace:') or sline.startswith('form:'):
                prefix = 'replace:' if sline.startswith('replace:') else 'form:'
                raw_rep = sline.replace(prefix, '').strip().strip('"').strip("'")
                if raw_rep and raw_rep != '|':
                    current_replace.append(raw_rep)
            elif current_trigger and not sline.startswith('- trigger:'):
                if sline:
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
            matches = parse_yaml_matches(filepath)
            for trigger, replace in matches:
                clean_replace = replace.replace('\n', ' ').strip()
                # Clean up double brackets for Unikey readability
                clean_replace = clean_replace.replace('[[', '[').replace(']]', ']')
                all_macros.append(f"{trigger}:{clean_replace}")

    with open(output_file, 'w', encoding='utf-8') as out:
        out.write("# UNIKEY / EVKEY MACRO TABLE FOR SOFTEL CHAT AGENT (ANTI-GRAVITY)\n")
        out.write("# Representative: Martin | Softel Solutions\n")
        out.write("# To use: Open Unikey -> Expand (Mở rộng) -> Check 'Enable Macro' (Bật tính năng gõ tắt)\n")
        out.write("# -> Click 'Macro Table' (Bảng gõ tắt) -> Select or paste content from this file.\n")
        out.write("\n".join(all_macros))
        out.write("\n")

    print(f"Đã xuất thành công {len(all_macros)} phím tắt Anti-Gravity sang file: {output_file}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
