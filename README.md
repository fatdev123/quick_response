# Softel Solutions - Anti-Gravity Master Operating System
> **AirTalk Wireless & TAG Mobile (US Lifeline / ACP Ecosystem)**  
> *Representative: Martin | Triết lý: Zero Fatal Errors | Cognitive Relief | Instant Empathy | Dynamic Forms*

---

## 📌 1. TỔNG QUAN HỆ THỐNG "ANTI-GRAVITY"

Hệ thống Master **"Anti-Gravity" (Triệt Tiêu Trọng Lực Vận Hành)** được thiết kế nhằm loại bỏ hoàn toàn ma sát tâm lý, quá tải nhận thức và các lỗi chí mạng (Fatal QA Errors) cho đội ngũ CSR Chat Agent tại Softel Solutions.

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                          TRIẾT LÝ VẬN HÀNH "ANTI-GRAVITY"                               │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Zero Fatal Errors    │ Đóng gói 100% quy định FCC/USAC/SLA vào mẫu tin nhắn chuẩn.  │
│ 2. Cognitive Relief     │ Chuyển thao tác gõ thủ công sang gõ tắt linh hoạt 3-Zone Lego.│
│ 3. Instant Empathy      │ Tự động hóa lời xoa dịu [RED Zone] trong mọi tình huống.     │
│ 4. Dynamic Variable     │ Điền tự động biến [[ticket_id]], [[port_out_pin]], [[reason]]. │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📂 2. CẤU TRÚC THƯ MỤC HỆ THỐNG

```
e:\softel\
├── .gitignore                          # Loại trừ file PDF/DOCX nội bộ, chỉ quản lý code & docs
├── README.md                           # Tài liệu tổng quan & hướng dẫn vận hành
├── unikey_macro.txt                    # Bảng 168 phím tắt tương thích 100% Unikey / EVKey
│
├── cheatsheet/                         # Cẩm nang tác chiến cho CSR
│   ├── MASTER_POLICY_MATRIX.md         # Ma trận SLA chuẩn hóa 8 trụ cột (Đã sửa sai lệch)
│   ├── SOFTEL_INTERNAL_SOP_DEEP_DIVE.md# Phân tích chuyên sâu 10 phân hệ từ 57 tài liệu nội bộ
│   ├── QA_SURVIVAL_PLAYBOOK.md         # Chiến lược phòng thủ 100 điểm QA & Anti-Evasion
│   ├── RAPID_LOOKUP_CTRL_F.md          # Cẩm nang tra cứu 3 bước siêu tốc
│   └── CONCURRENCY_WORKFLOW.md         # Băng chuyền 3 giai đoạn xử lý 3-5 chat cùng lúc
│
├── espanso/                            # Kho cấu hình Snippet cho Espanso (YAML)
│   ├── config/
│   │   └── default.yml                 # Cấu hình Clipboard và shortcut
│   └── match/
│       ├── airtalk_tag_master.yml      # Master 3-Zone Lego (:atw-) chuẩn QA (62 snippets)
│       ├── base_system.yml             # Chào hỏi, Hold 1-2p, Cảnh báo thô tục (16 snippets)
│       ├── verification_cpni.yml       # Xác thực CPNI, ID proof, Address (11 snippets)
│       ├── red_empathy.yml             # Kho Vùng Đỏ: Đồng cảm theo loại sự cố (13 snippets)
│       ├── yellow_policy.yml           # Kho Vùng Vàng: Chính sách & Giới hạn (28 snippets)
│       ├── green_solution.yml          # Kho Vùng Xanh: Giải pháp & Hành động (24 snippets)
│       └── combos_speed.yml            # Combo 1-Hit cho giờ cao điểm (14 snippets)
│
└── scripts/                            # Bộ công cụ tự động hóa
    ├── validate_snippets.py            # Kiểm toán cú pháp & chống trùng lặp (168 snippets)
    ├── export_unikey.py                # Tự động xuất snippet sang bảng Macro Unikey
    └── sync_espanso.py                 # Tự động đồng bộ config vào AppData của Espanso
```

---

## ⚡ 3. BẢNG MA TRẬN KHẮC PHỤC SAI LỆCH SLA/POLICY (PHÒNG THỦ FATAL QA)

Hệ thống "Anti-Gravity" đã sửa triệt để các sai lệch so với SOP nội bộ:

| Phân Hệ Nghiệp Vụ | Sai Lệch Trước Đây (Rất Nguy Hiểm) ❌ | Thông Số Chuẩn Theo SOP Mới Nhất ✅ |
| :--- | :--- | :--- |
| **Hoàn Tiền (Refund)** | Cào bằng 7 ngày cho mọi loại máy. | • **Free Pre-Owned:** 15 ngày từ ngày nhận.<br>• **Brand-New & Paid Pre-Owned:** 30 ngày từ ngày nhận.<br>• **Non-Defective:** 7 ngày (khách chịu ship).<br>• **ILD/Data/Monthly fee:** Không hoàn tiền. |
| **Bảo Hành (Warranty)** | Bảo hành duy nhất 15 ngày cho mọi máy. | • **Free Pre-Owned & Phụ kiện:** 15 ngày.<br>• **Brand-New & Paid Upgrade:** 30 ngày.<br>• **Hư hỏng vật lý/rơi vỡ:** Phải báo trong **48 giờ** từ lúc giao.<br>• **Return Label:** Gửi bưu điện trong **7 ngày làm việc**. |
| **Cam Kết Trợ Giá (Device Subsidy)** | Báo cam kết 365 ngày. | • **Cam kết trợ giá thiết bị:** Đúng **180 ngày** active liên tục. |
| **Mã Chuyển Mạng (Port-Out PIN)** | Chỉ báo hạn 4 ngày, thiếu cảnh báo. | • Mã PIN hạn **4 ngày**.<br>• Cảnh báo phí vi phạm cam kết trợ giá nếu < 180 ngày.<br>• Cảnh báo mất vĩnh viễn số nếu bị de-enroll do non-usage. |
| **Non-Usage (NUC)** | 30 ngày + 15 ngày (45 ngày). | • 30 ngày inactive + 15 ngày notice.<br>• Ngày 46 de-enroll, **cập nhật NLAD trong 1 ngày làm việc**. |

---

## 🚀 4. DANH MỤC PHÍM TẮT MASTER :ATW- (QA APPROVED)

### 🔹 Vận Hành Cốt Lõi & Phòng Thủ QA
- `:atw-hi` : Chào hỏi khách hàng (*"My name is Martin. How may I assist you with your service?"*).
- `:atw-cpni-ask` : Yêu cầu xác minh 3 yếu tố CPNI: Full Name, DOB, SSN4.
- `:atw-cpni-pass` : Thông báo xác thực thành công.
- `:atw-cpni-fail` : Từ chối cung cấp thông tin tài khoản khi sai CPNI (chống mớm dữ liệu).
- `:atw-hold-check` : Xin phép kiểm tra hệ thống 1–2 phút (*Reset đồng hồ ART*).
- `:atw-wrapup` : Câu hỏi kết thúc ca chuẩn QA.
- `:atw-crm-note` : Biểu mẫu điền Activity Log trên CRM tự động.

### 🔹 8 Kịch Bản Nghiệp Vụ Sinh Tử
1. **Hot Rush Ticket & Out of Stock:** `:atw-rush-red`, `:atw-rush-ylw`, `:atw-rush-grn` (Form Ticket ID), `:atw-rush-combo`.
2. **Lost/Stolen & Blacklist IMEI:** `:atw-lost-red`, `:atw-lost-ylw` (Hạn báo 48h), `:atw-lost-grn`, `:atw-lost-combo`.
3. **Return to Sender (RTS):** `:atw-rts-red`, `:atw-rts-ylw` (Hạn 10 ngày POA), `:atw-rts-grn`, `:atw-rts-combo`.
4. **Cancel Port-Out & Winback:** `:atw-winback-red`, `:atw-winback-ylw` (Cam kết 180 ngày), `:atw-winback-grn`, `:atw-winback-combo`.
5. **Identity Theft & Slamming:** `:atw-fraud-red`, `:atw-fraud-ylw` (USAC Hotline 1-800-234-9473), `:atw-fraud-grn`, `:atw-fraud-combo`.
6. **Loyalty Program & Referral:** `:atw-loyalty-red`, `:atw-loyalty-ylw` (2 pts/tháng, Thổ dân 5 pts/tháng), `:atw-loyalty-grn`, `:atw-loyalty-combo`.
7. **ILD & Cấm Roaming:** `:atw-ild-red`, `:atw-ild-ylw` (Cấm Roaming quốc tế, cước ILD không hoàn tiền), `:atw-ild-grn`, `:atw-ild-combo`.
8. **Voicemail Setup:** `:atw-vm-red`, `:atw-vm-ylw`, `:atw-vm-grn` (Reset PIN về 4 số cuối MDN), `:atw-vm-combo`.
9. **Chống Né Tránh Điều Tra Spam:** `:atw-spam-evasion` (Phong tỏa yêu cầu đổi số/mua SIM khi đang điều tra Spam).

---

## 🛠️ 5. HƯỚNG DẪN CÀI ĐẶT & SỬ DỤNG

### Cách 1: Sử Dụng Phần Mềm Espanso (Khuyến Nghị Tối Đa)
1. Cài đặt Espanso qua Windows Terminal:
   ```powershell
   winget install Espanso.Espanso -e
   ```
2. Đồng bộ toàn bộ 168 phím tắt vào Espanso:
   ```powershell
   python scripts\sync_espanso.py
   ```
3. Mở Espanso và gõ thử `:atw-hi` hoặc `:atw-rush-combo` trên bất kỳ cửa sổ chat nào.

### Cách 2: Sử Dụng Unikey / EVKey
1. Mở file [unikey_macro.txt](file:///e:/softel/unikey_macro.txt).
2. Vào **Unikey** -> **Mở rộng** -> Bật **Bảng gõ tắt...** và nạp toàn bộ 168 macro vào.
