# CẨM NANG PHÒNG THỦ ĐIỂM QA "ANTI-GRAVITY"
*(Bảo vệ 100 Điểm Chất Lượng - Triệt Tiêu 100% Lỗi Chí Mạng / Fatal Errors)*
*CSR: Martin | Softel Solutions - AirTalk Wireless & TAG Mobile*

---

## 1. TRIẾT LÝ VẬN HÀNH "ANTI-GRAVITY" (TRIỆT TIÊU TRỌNG LỰC VẬN HÀNH)

1. **Zero Fatal Errors:** Đóng gói 100% quy định FCC/USAC/SLA vào mẫu tin nhắn chuẩn; loại bỏ hoàn toàn rủi ro cam kết sai (False Promise).
2. **Cognitive Relief:** Chuyển thao tác gõ thủ công và ghi nhớ hàng trăm con số chính sách sang hệ thống phím tắt 3-Zone Lego linh hoạt.
3. **Instant Empathy:** Tự động hóa lời xoa dịu Vùng Đỏ `[RED Empathy]` trong 100% mọi tình huống trước khi đưa ra chính sách hay giải pháp.
4. **Dynamic Variable:** Tự động hóa điền các biến số động `[[ticket_id]]`, `[[port_out_pin]]`, `[[reason]]` mà không để lại ký tự giữ chỗ thô cứng.

---

## 2. BẢNG TIÊU CHÍ CHẤM ĐIỂM QA & BỌC LÓT BẰNG SNIPPET :ATW-

Trong kiểm toán chất lượng tại Softel Solutions, hệ thống áp dụng 3 nhóm lỗi chí mạng. Vi phạm **1 lỗi duy nhất = 0 điểm (Auto-Fail / Fatal)**:

| Nhóm Tiêu Chí QA | Trọng Số | Các Lỗi Điểm Liệt (Fatal Errors) | Cách Bọc Lót Tuyệt Đối Bằng Snippet :atw- |
| :--- | :--- | :--- | :--- |
| **1. CPNI & Security Verification** | **30% (Chí Mạng)** | • Tiết lộ thông tin tài khoản khi chưa xác thực Full Name, DOB, SSN4.<br>• Mớm thông tin đúng khi khách đoán sai.<br>• Cấp Port-out PIN hoặc đổi địa chỉ khi chưa pass verification. | • Gõ ngay `:atw-cpni-ask` ở tin nhắn thứ 2.<br>• Nếu sai thông tin: Gõ ngay `:atw-cpni-fail` (tuyệt đối không mớm dữ liệu).<br>• Pass thành công: Gõ `:atw-cpni-pass`. |
| **2. Cam Kết Sai Policy & SLA (False Promise)** | **25% (Chí Mạng)** | • Tự ý hứa hoàn tiền ngay không qua Accounting.<br>• Hứa gửi máy mới trong ngày không qua Logistics.<br>• Báo sai thời hạn mã Port-out PIN (nói 30 ngày thay vì 4 ngày).<br>• Báo sai hạn cam kết trợ giá (nói 365 ngày thay vì 180 ngày).<br>• Bỏ sót mốc báo hỏng màn hình/vật lý trong 48 giờ. | Sử dụng các mẫu Vùng Vàng chuẩn SOP đã audit:<br>• `:atw-refund-ylw` (15d pre-owned, 30d paid/brand-new, 7d non-defective).<br>• `:atw-war-ylw` (15d/30d/48h cosmetic defect).<br>• `:atw-po-ylw` (4d PIN, cam kết 180d trợ giá).<br>• `:atw-nonuse-ylw` (30+15=45d, NLAD 1d). |
| **3. Thái Độ & Ngắt Chat Trái Quy Định** | **20% (Chí Mạng)** | • Ngắt chat khi khách đang nói mà chưa cảnh báo.<br>• Tranh cãi, mỉa mai, công kích khách.<br>• Phớt lờ cảm xúc tiêu cực của khách. | • Mở đầu bằng Vùng Đỏ: `:atw-deescalate`.<br>• Đưa ra cảnh báo lịch sự: `:atw-warn-profanity`.<br>• Chỉ ngắt kết nối sau cảnh báo bằng: `:atw-disconnect`. |
| **4. Thời Gian Phản Hồi (FRT / ART)** | **15%** | • Để khách đợi quá 90 giây không có tin nhắn trấn an.<br>• Lần phản hồi đầu tiên (FRT) > 60 giây. | Gõ `:atw-hold-check` mỗi 45–60 giây để làm mới đồng hồ đếm ngược ART trên hệ thống. |
| **5. Chốt Ca & Ghi Chú CRM** | **10%** | • Không hỏi *"Is there anything else I can assist you with?"* trước khi đóng.<br>• Không cập nhật Activity Log / Phân loại sai lý do Ticket. | • Gõ câu chốt chuẩn: `:atw-wrapup` và `:atw-bye`.<br>• Chèn sẵn mẫu ghi chú Activity Log trên CRM: `:atw-crm-note`. |

---

## 3. CHIẾN THUẬT BĂNG CHUYỀN 3 GIAI ĐOẠN (CONCURRENCY 3–5 CHATS)

Khi ca trực bước vào giờ cao điểm, để tránh nhầm lẫn thông tin giữa các khách hàng (lỗi rò rỉ CPNI nghiêm trọng) và duy trì ART < 90 giây, CSR Martin áp dụng nguyên tắc:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. NHÓM ĐẦU VÀO (INBOUND - 0 đến 30s đầu)                                   │
│    • Mục tiêu: Đạt chuẩn FRT < 20s.                                         │
│    • Thao tác: Gõ ngay :atw-hi + :atw-cpni-ask. Thao tác trong 3 giây.      │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. NHÓM TRA CỨU & XỬ LÝ (PROCESSING - Đang kiểm tra CRM)                    │
│    • Mục tiêu: Giữ chân khách không bị im lặng quá 60s.                     │
│    • Thao tác: Cứ 45s gõ :atw-hold-check để làm mới đồng hồ ART.            │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. NHÓM KẾT QUẢ & CHỐT CA (OUTPUT & RESOLUTION)                             │
│    • Mục tiêu: Ghép Lego [Yellow Policy] + [Green Solution] giải quyết dứt điểm.│
│    • Thao tác: Gõ combo theo case (ví dụ :atw-po-combo, :atw-rush-combo).   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. CHIẾN THUẬT PHÒNG THỦ CHỐNG NÉ ĐIỀU TRA SPAM (SPAM EVASION DEFENSE)

Theo SOP Spam Handling V2.2, khi tài khoản bị gắn cờ Spam Investigation, khách hàng thường cố tình tạo các yêu cầu giả nhằm né tránh việc nộp ID/Video xác minh:
1. Yêu cầu đổi số điện thoại (MDN Change).
2. Đòi mua SIM mới với số mới.
3. Báo mất máy / mất SIM (Lost/Stolen).
4. Báo kiện hàng Delivered nhưng không nhận được (DCNR).

> [!CAUTION]
> **QUY TẮC PHÒNG THỦ:** Khi tài khoản đang trong trạng thái Spam Investigation, **TẤT CẢ các yêu cầu trên đều phải tạm dừng**. CSR tuyệt đối không được bypass hệ thống để đặt SIM hay đổi số.
> Bắt buộc dùng trigger `:atw-spam-evasion`:
> *"I understand you are requesting a change to your line. However, because your account is currently under an active Spam Security Investigation, our system automatically restricts account modifications including new SIM orders, phone number changes, or line transfers until verification is completed. Please submit your clear photo ID holding next to your face so our Fraud Review Team can inspect your file within 24 to 48 business hours and restore full access to your account."*

---

## 5. LỘ TRÌNH TRIỂN KHAI "ANTI-GRAVITY" 4 GIAI ĐOẠN

```
Phase 1 (Ngày 1–3)   : Đóng gói & Thẩm định Mã nguồn YAML Cấu hình Espanso (:atw- Master).
Phase 2 (Ngày 4–7)   : Đào tạo Mô phỏng Thực chiến (Sandbox Training) cho CSR theo Lego 3-Zone.
Phase 3 (Ngày 8–10)  : Cài đặt Đồng bộ Espanso / Unikey trên toàn bộ máy tính trực.
Phase 4 (Ngày 11–14) : Kiểm toán QA Hàng ngày & Tối ưu hóa Chỉ số AHT/CSAT (Về 0% Fatal Error).
```
