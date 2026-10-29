# CẨM NANG PHÒNG THỦ ĐIỂM QA (QA SURVIVAL PLAYBOOK)
*(Bảo vệ 100 Điểm Chất Lượng - Triệt Tiêu Lỗi Chí Mạng / Fatal Errors)*

---

## 1. BẢNG TIÊU CHÍ CHẤM ĐIỂM QA & NGUY CƠ ĐIỂM LIỆT (FATAL TRAPS)

Trong đánh giá chất lượng cuộc chat (Chat QA Assessment) tại Softel, có 3 nhóm lỗi chí mạng mà chỉ cần mắc **1 lỗi duy nhất** là cả bài kiểm tra bị **0 điểm (Auto-Fail / Fatal)**:

| Nhóm Tiêu Chí | Trọng Số | Các Lỗi Điểm Liệt (Auto-Fail / Fatal Errors) | Cách Khắc Phục Bằng Lego Snippet |
| :--- | :--- | :--- | :--- |
| **1. CPNI & Security Verification** | **30% (Chí Mạng)** | • Tiết lộ thông tin tài khoản khi chưa xác thực Full Name, DOB, SSN4.<br>• Mớm thông tin đúng khi khách đoán sai.<br>• Cung cấp Port-out PIN hoặc đổi địa chỉ khi chưa pass verification. | Dùng ngay `;v_cpni` ở tin nhắn thứ 2.<br>Nếu sai dùng ngay `;v_fail` (tuyệt đối không gợi ý). |
| **2. Cam Kết Sai Policy & SLA (False Promise)** | **25% (Chí Mạng)** | • Tự ý hứa hoàn tiền ngay lập tức (không qua Accounting).<br>• Tự hứa gửi máy mới ngay trong ngày mà không qua quy trình rà soát kho/Logistics.<br>• Báo sai thời hạn mã Port-out PIN (bảo có hạn 30 ngày thay vì 4 ngày). | Dùng các mẫu Vùng Vàng chuẩn: `;y_po_pin`, `;y_refund`, `;y_war15`, `;y_dcnr`. |
| **3. Thái Độ & Ngắt Chat Trái Quy Định (Conduct & Disconnect)** | **20% (Chí Mạng)** | • Đóng khung chat khi khách đang nói mà chưa cảnh báo.<br>• Tranh cãi tay đôi, dùng từ mỉa mai, công kích khách.<br>• Phớt lờ cảm xúc tiêu cực của khách hàng. | Dùng các mẫu Vùng Đỏ `;r_angry`, `;r_profanity` để hạ nhiệt và đưa ra cảnh báo chuẩn mực. |
| **4. Thời Gian Phản Hồi (FRT / ART)** | **15%** | • Để khách đợi quá 90 giây không có tin nhắn trấn an.<br>• FRT lần đầu > 60 giây. | Gõ `;h_check` mỗi 45-60 giây để làm mới đồng hồ ART. |
| **5. Chốt Ca & Ghi Chú (Closing & CRM Logging)** | **10%** | • Không hỏi *"Is there anything else I can assist you with?"* trước khi đóng ca.<br>• Không cập nhật Activity Log / Phân loại sai lý do Ticket. | Dùng `;wrap_up` và lưu sẵn mẫu ghi chú ticket `;crm_note`. |

---

## 2. KỊCH BẢN XỬ LÝ KHÁCH HÀNG GIẬN DỮ & CHỬI BỚI (DE-ESCALATION PROTOCOL)

Khi khách hàng bắt đầu dùng lời lẽ thô tục hoặc đe dọa khiếu nại lên FCC/Luật sư:

### Bước 1: Không tự ái cá nhân & Lắng nghe cảm xúc (De-escalation First)
Khách hàng không giận bạn, họ đang giận hệ thống hoặc sự cố gián đoạn ảnh hưởng đến cuộc sống của họ.
- **Trigger:** `;r_deescalate`
- **Mẫu câu:** *"I completely hear your frustration, and I am genuinely sorry for the trouble this has caused you. I am here to take ownership of this issue and work with you step-by-step toward a resolution."*

### Bước 2: Thiết lập ranh giới lịch sự (Professional Warning)
Nếu khách hàng tiếp tục lăng mạ hoặc dùng từ ngữ xúc phạm nặng nề:
- **Trigger:** `;r_warning`
- **Mẫu câu:** *"I truly want to help you resolve this issue today; however, I kindly ask that we keep our conversation respectful. Please avoid using profanity so that we can focus on getting this solved for you."*

### Bước 3: Đóng chat theo quy chuẩn nếu khách tiếp tục quá khích (Safe Disconnect)
Chỉ được ngắt kết nối sau khi đã đưa ra ít nhất 1 cảnh báo lịch sự:
- **Trigger:** `;r_disconnect`
- **Mẫu câu:** *"Since the abusive language has continued, I will be closing this chat session now. You may reach back out to us at any time when you are ready to continue in a professional manner. Have a good day."*

---

## 3. CHECKLIST 5 BƯỚC HOÀN THIỆN MỘT CA CHAT ĐẠT 100 ĐIỂM

```
[ ] BƯỚC 1: Chào hỏi chuyên nghiệp & Xác thực CPNI đầy đủ 3 thông số (Full Name, DOB, SSN4).
[ ] BƯỚC 2: Thu thập Email và Callback Number để phòng mất kết nối.
[ ] BƯỚC 3: Đồng cảm ngay khi khách nêu vấn đề (Red Zone) trước khi giải thích quy định.
[ ] BƯỚC 4: Báo đúng mốc thời gian SLA (Yellow Zone) và đưa ra hành động cụ thể (Green Zone).
[ ] BƯỚC 5: Hỏi câu hỏi chốt ca chuẩn, cập nhật Activity Log và phân loại Ticket chính xác trên CRM.
```
