#!/usr/bin/env python3
"""
Sync Script: Đồng bộ cấu hình từ Repository vào thư mục cài đặt của Espanso trên Windows.
Đích đến: %APPDATA%\\espanso\\match\\ và %APPDATA%\\espanso\\config\\
"""

import os
import sys
import shutil
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_config_dir = os.path.join(base_dir, 'espanso', 'config')
    src_match_dir = os.path.join(base_dir, 'espanso', 'match')
    
    appdata = os.environ.get('APPDATA')
    if not appdata:
        print("Lỗi: Không tìm thấy biến môi trường APPDATA!")
        sys.exit(1)
        
    espanso_dir = os.path.join(appdata, 'espanso')
    dst_config_dir = os.path.join(espanso_dir, 'config')
    dst_match_dir = os.path.join(espanso_dir, 'match')
    
    os.makedirs(dst_config_dir, exist_ok=True)
    os.makedirs(dst_match_dir, exist_ok=True)
    
    print("=" * 60)
    print("ĐỒNG BỘ CẤU HÌNH ESPANSO CHO SOFTEL CHAT AGENT")
    print("=" * 60)
    print(f"Thư mục nguồn (Repo): {base_dir}")
    print(f"Thư mục đích (Espanso): {espanso_dir}")
    print("-" * 60)
    
    # Copy config files
    if os.path.exists(src_config_dir):
        for f in os.listdir(src_config_dir):
            if f.endswith(('.yml', '.yaml')):
                s = os.path.join(src_config_dir, f)
                d = os.path.join(dst_config_dir, f)
                shutil.copy2(s, d)
                print(f"[OK] Đã chép config: {f}")
                
    # Copy match files
    if os.path.exists(src_match_dir):
        for f in os.listdir(src_match_dir):
            if f.endswith(('.yml', '.yaml')):
                s = os.path.join(src_match_dir, f)
                d = os.path.join(dst_match_dir, f)
                shutil.copy2(s, d)
                print(f"[OK] Đã chép snippet: {f}")
                
    print("-" * 60)
    print("Đã hoàn tất đồng bộ toàn bộ file cấu hình vào Espanso!")
    
    # Try restarting espanso if available
    try:
        res = subprocess.run(["espanso", "restart"], capture_output=True, text=True)
        if res.returncode == 0:
            print("[*] Đã tự động khởi động lại Espanso thành công!")
        else:
            print("[*] Espanso chưa chạy. Bạn có thể khởi động Espanso để bắt đầu dùng.")
    except FileNotFoundError:
        print("[*] Lưu ý: Lệnh 'espanso' chưa có trong PATH hoặc chưa được cài đặt.")
        print("    Bạn có thể cài đặt bằng lệnh: winget install Espanso.Espanso -e")
        
    print("=" * 60)
    return 0

if __name__ == '__main__':
    sys.exit(main())
