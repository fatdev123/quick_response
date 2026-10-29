# Softel Solution - Chat Agent Operating System
> **AirTalk Wireless & TAG Mobile (US Lifeline / ACP Ecosystem)**  
> *Hệ thống phím tắt thông minh, tư duy 3 Vùng (Red - Yellow - Green), tra cứu nghiệp vụ siêu tốc và cẩm nang phòng thủ điểm QA.*

---

## 📌 1. TỔNG QUAN HỆ THỐNG

Kho lưu trữ này được xây dựng nhằm giải phóng hoàn toàn đôi bàn tay cho **CSR Chat Agent** tại Softel Solution, giải quyết triệt để áp lực xử lý đồng thời 3–5 ca chat trên LiveChat và CRM Portal giữa "biển chính sách" (hơn 70 SOPs & Policies).

### Cốt Lõi: Mindset Xử Lý 3 Vùng (The 3-Zone Framework)
Toàn bộ phản hồi gửi tới khách hàng Mỹ được cấu trúc thành 3 mảnh ghép Lego:
1. **Vùng Đỏ (Red Zone - Empathy):** Ghi nhận cảm xúc, đồng cảm sâu sắc với sự cố của khách, hạ nhiệt bức xúc *(Tuyệt đối không giải thích điều khoản tại vùng này)*.
2. **Vùng Vàng (Yellow Zone - Policy & Limits):** Nêu rõ nguyên nhân, giới hạn kỹ thuật và quy định pháp lý/công ty ngắn gọn *(Hệ thống LÀM ĐƯỢC gì và KHÔNG LÀM ĐƯỢC gì)*.
3. **Vùng Xanh (Green Zone - Solution & Commitment):** Đưa ra các bước hành động cụ thể, hướng dẫn thao tác kèm mốc thời gian cam kết rõ ràng (SLA/TAT).

$$\text{Tin Nhắn Chuẩn QA} = \mathbf{Red}\ (\text{Đồng cảm}) + \mathbf{Yellow}\ (\text{Quy định}) + \mathbf{Green}\ (\text{Giải pháp/Hẹn giờ})$$

---

## 📂 2. CẤU TRÚC THƯ MỤC

```
e:\softel\
├── .gitignore                      # Loại trừ file PDF/DOCX dung lượng lớn
├── README.md                       # Tài liệu hướng dẫn sử dụng & vận hành
├── unikey_macro.txt                # File gõ tắt tương thích 100% Unikey / EVKey
│
├── cheatsheet/                     # Cẩm nang cất cánh cho Agent
│   ├── MASTER_POLICY_MATRIX.md     # Ma trận 7 phân hệ chính sách cốt lõi & SLA
│   ├── RAPID_LOOKUP_CTRL_F.md      # Quy trình 3 bước xử lý case lạ & từ khóa Ctrl+F
│   ├── QA_SURVIVAL_PLAYBOOK.md     # Checklist phòng ngừa lỗi chí mạng (Fatal Errors)
│   └── CONCURRENCY_WORKFLOW.md     # Chiến thuật băng chuyền xử lý 3-5 chat cùng lúc
│
├── espanso/                        # Kho cấu hình Snippet cho Espanso (YAML)
│   ├── config/
│   │   └── default.yml             # Cấu hình clipboard và phím tắt
│   └── match/
│       ├── base_system.yml         # Chào hỏi, Hold 1-2p, Cảnh báo thô tục, Chốt ca
│       ├── verification_cpni.yml   # Xác thực Full Name, DOB, SSN4, ID Proof
│       ├── red_empathy.yml         # Kho Lego Vùng Đỏ (Đồng cảm theo từng loại sự cố)
│       ├── yellow_policy.yml       # Kho Lego Vùng Vàng (Chính sách, mốc 4d, 7d, 15d, 45d)
│       ├── green_solution.yml      # Kho Lego Vùng Xanh (Khắc phục sự cố, Tạo ticket)
│       └── combos_speed.yml        # Combo 3 Vùng 1-Hit cho giờ cao điểm
│
└── scripts/                        # Bộ công cụ tự động hóa
    ├── validate_snippets.py        # Kiểm tra tính toàn vẹn và chống trùng lặp trigger
    ├── export_unikey.py            # Tự động xuất snippet sang bảng Macro Unikey
    └── sync_espanso.py             # Tự động đồng bộ config vào AppData của Espanso
```

---

## ⚡ 3. HƯỚNG DẪN CÀI ĐẶT & SỬ DỤNG

### Cách 1: Sử Dụng Phần Mềm Espanso (Khuyến Nghị Tối Đa)
1. **Cài đặt Espanso qua Windows Terminal (PowerShell):**
   ```powershell
   winget install Espanso.Espanso -e
   ```
2. **Đồng bộ cấu hình từ thư mục này vào Espanso:**
   ```powershell
   python scripts\sync_espanso.py
   ```
3. **Khởi động Espanso:** Mở Menu Start gõ `Espanso` và bật chạy. Bấm thử `;hi` hoặc `;v_cpni` trên bất kỳ khung chat nào để kiểm tra kết quả!

---

### Cách 2: Sử Dụng Unikey / EVKey (Không Cần Quyền Administrator)
Nếu máy tính công ty không cho phép cài phần mềm ngoài:
1. Mở file `unikey_macro.txt` có sẵn trong thư mục gốc.
2. Bật bảng điều khiển **Unikey** -> Chọn **Mở rộng** -> Tích chọn **Bật tính năng gõ tắt**.
3. Bấm nút **Bảng gõ tắt...** -> Nạp toàn bộ danh sách từ file `unikey_macro.txt` vào.
4. Bấm **Lưu** và gõ thử các phím tắt bình thường.

---

## 🚀 4. HƯỚNG DẪN ĐẨY LÊN GITHUB REPOSITORY CÁ NHÂN

Để quản lý và đồng bộ kho script này trên GitHub cá nhân:

1. **Khởi tạo Git cục bộ:**
   ```powershell
   cd e:\softel
   git init
   git add .
   git commit -m "feat: initial commit softel chat agent operating system"
   ```
2. **Tạo một Repository mới trên GitHub (khuyến nghị để chế độ Private):**
   - Đặt tên repo, ví dụ: `softel-chat-os`.
3. **Liên kết và Đẩy mã nguồn lên GitHub:**
   ```powershell
   git branch -M main
   git remote add origin https://github.com/<tai-khoan-cua-ban>/softel-chat-os.git
   git push -u origin main
   ```
4. **Khi làm việc trên máy khác:** Chỉ cần `git clone` về máy và chạy `python scripts\sync_espanso.py` là có ngay toàn bộ kho đạn phím tắt!

---

## 📋 5. BẢNG PHÍM TẮT ĐỈNH CAO (QUICK SNIPPET CHEAT SHEET)

### 🔹 Nhóm Cơ Bản & Kiểm Soát Ca Chat (Base & Hold)
- `;hi` : Chào hỏi chuẩn chuyên nghiệp.
- `;h_check` : Xin phép kiểm tra hệ thống 1-2 phút (Reset ART timer).
- `;h_still` : Trấn an khách vẫn đang tra cứu hồ sơ.
- `;h_lead` : Xin phép tham vấn ý kiến Senior / Supporter.
- `;wrap` : Câu hỏi kết thúc ca chuẩn QA: *"Is there anything else I can help you with?"*
- `;bye` : Lời chào tạm biệt chuyên nghiệp.
- `;r_deescalate` : Xoa dịu khách hàng đang bức xúc, cam kết hỗ trợ.
- `;r_warning` : Cảnh báo lịch sự khi khách dùng từ ngữ thô tục.
- `;r_disconnect` : Ngắt chat đúng quy chuẩn khi khách tiếp tục quá khích.

### 🔹 Nhóm Xác Minh CPNI & An Ninh (Security Verification)
- `;v_cpni` : Yêu cầu xác thực bắt buộc: Full Name + DOB + SSN4.
- `;v_contact` : Thu thập Email và Số điện thoại liên hệ lại.
- `;v_pass` : Thông báo xác thực thành công, sẵn sàng hỗ trợ.
- `;v_fail` : Từ chối cung cấp thông tin tài khoản do sai CPNI.
- `;v_id_photo` : Hướng dẫn gửi ảnh chụp cầm ID sát mặt.
- `;v_id_video` : Hướng dẫn gửi video 5-10s đọc tên + ngày sinh (Spam review).

### 🔹 Nhóm Combo 1-Hit Cho Giờ Cao Điểm (Combos Speed)
- `;c_dcnr` : Trọn gói xử lý kiện hàng Delivered nhưng không thấy máy (GPS trace 24-48h).
- `;c_lit` : Trọn gói xử lý bưu kiện kẹt tracking quá 7 ngày (Lost in transit).
- `;c_po` : Trọn gói cấp Port-Out PIN (Cảnh báo hạn 4 ngày, rà soát 24h).
- `;c_refund_late` : Trọn gói từ chối hoàn tiền lịch sự sau 7 ngày kèm giải pháp đổi máy.
- `;c_war_free` : Trọn gói bảo hành máy Free Lifeline 15 ngày + gửi return label 7 ngày.
- `;c_cancel` : Trọn gói giữ chân khách hàng (Retention) cảnh báo mất số/trợ cấp trước khi chuyển Tier 2.
- `;c_network` : Hướng dẫn khởi động lại máy, tháo lắp SIM và chờ kết quả.
- `;c_nonuse` : Giải thích luật Lifeline 30+15=45 ngày và hướng dẫn thực hiện cước ngay.
- `;c_spam` : Hướng dẫn quy trình gửi hồ sơ gỡ chặn nghi ngờ spam.

---
*Tài liệu được thiết kế chuyên biệt cho CSR Softel Solution - Bảo mật nội bộ & Tối ưu hóa hiệu suất.*
