# CHIẾN THUẬT QUẢN LÝ ĐA NHIỆM (CONCURRENCY CHAT WORKFLOW)
*(Bí Kíp Xử Lý 3 – 5 Chat Cùng Lúc Giữa LiveChat & Portal CRM Nội Bộ Mà Không Rối Não)*

---

## 1. THÁCH THỨC CỦA CHAT AGENT ĐA NHIỆM

Khi ca trực bước vào giờ cao điểm (Peak Hours), mỗi Agent tại Softel phải gánh đồng thời **3 đến 5 cửa sổ chat song song**.
- Cửa sổ 1: Khách đang chửi bới vì FedEx báo giao rồi mà không thấy máy (DCNR).
- Cửa sổ 2: Khách đòi lấy Port-out PIN chuyển mạng gấp.
- Cửa sổ 3: Khách mới vào, chưa xác thực CPNI.
- Cửa sổ 4: Khách bị gián đoạn sóng (Service Issue), yêu cầu bồi thường tiền.

Nếu gõ thủ công bằng tay hoặc nhớ nhớ quên quên, Agent sẽ:
- **Nhầm lẫn thông tin:** Gửi mã PIN của khách này sang cho khách kia (Lỗi rò rỉ CPNI nghiêm trọng).
- **Trễ thời gian phản hồi (ART > 90s):** Bị hệ thống LiveChat tính điểm trừ tốc độ phản hồi.
- **Não bộ quá tải:** Căng thẳng tột độ và dễ nổi nóng với khách.

---

## 2. QUY TẮC "BĂNG CHUYỀN 3 GIAI ĐOẠN" (THE 3-STAGE CONVEYOR BELT)

Chia tất cả các cuộc chat đang mở thành 3 nhóm trạng thái trên màn hình:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. NHÓM ĐẦU VÀO (INBOUND - 0 đến 30 giây đầu)                               │
│ • Mục tiêu: Đạt chuẩn FRT < 20s.                                            │
│ • Thao tác: Gõ ngay ;hi + ;v_cpni hoặc ;h_check.                            │
│ • Thời gian thao tác: 3 GIÂY. Sau đó chuyển sang chat tiếp theo.            │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. NHÓM TRA CỨU & XỬ LÝ (PROCESSING - Đang kiểm tra CRM)                    │
│ • Mục tiêu: Giữ chân khách không bị im lặng quá 60s.                        │
│ • Thao tác: Mở tab CRM tra cứu. Cứ 45s gõ ;h_check để làm mới ART.          │
│ • Thời gian thao tác: 5 GIÂY mỗi chu kỳ gõ.                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. NHÓM KẾT QUẢ & CHỐT CA (OUTPUT & RESOLUTION)                             │
│ • Mục tiêu: Ghép Lego [Yellow Policy] + [Green Solution] giải quyết dứt điểm.│
│ • Thao tác: Gõ combo theo case (ví dụ ;c_po, ;c_dcnr, ;c_refund).           │
│ • Thời gian thao tác: 5 GIÂY.                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. NGUYÊN TẮC BẢO VỆ DỮ LIỆU ĐA NHIỆM (ANTI-MIXUP RULES)

1. **Quy tắc 1 Tab CRM - 1 Khách Hàng:**
   - Khi chat trên LiveChat / Portal, luôn copy Enrollment ID / MDN của khách dán vào thanh tìm kiếm CRM và mở đúng hồ sơ của khách đó.
   - Trước khi dán mã PIN hoặc thông tin cá nhân, **liếc mắt nhìn tên khách trên cửa sổ chat và tên trên CRM** xem có khớp nhau 100% hay không.
2. **Quy tắc "Không trả lời một nửa":**
   - Đừng gõ dở dang một câu dài rồi chuyển sang tab chat khác.
   - Hãy dùng **Lego Snippet**: Gõ từ khóa trigger (ví dụ `;c_po`) -> Snippet bung ra trọn vẹn câu trả lời -> Đọc lướt 2 giây -> Bấm Send. Sau đó mới chuyển tab.
3. **Quy tắc Giữ Chân Bằng Mốc Thời Gian Cụ Thể:**
   - Thay vì im lặng để tìm dữ liệu, luôn gửi tin nhắn thông báo:
     *";h_check"* -> *"I am currently reviewing your account details in our system. Please bear with me for about 1 to 2 minutes, and I will be right back with an update!"*
