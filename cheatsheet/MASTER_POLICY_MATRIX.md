# BẢNG MA TRẬN NGHIỆP VỤ CỐT LÕI - SOFTEL SOLUTIONS (ANTI-GRAVITY MASTER)
*(AirTalk Wireless & TAG Mobile - Lifeline / ACP / MVNO Ecosystem)*
*Dành riêng cho CSR Chat Agent: Martin | Triệt Tiêu Fatal QA | 100% Khớp SOP Nội Bộ*

---

## ⚡ PHẦN 0: MA TRẬN CHẨN ĐOÁN SAI LỆCH SLA/POLICY & PHÒNG THỦ FATAL QA

| Nhóm Quy Trình (SOP Module) | Thông Số Sai Lệch Thường Gặp (Bẫy QA) ❌ | Thông Số Chuẩn Theo SOP Nội Bộ Mới Nhất ✅ | Rủi Ro Vận Hành & Hậu Quả Audit QA |
| :--- | :--- | :--- | :--- |
| **Chính Sách Hoàn Tiền (Refund Policy)** | Áp dụng cào bằng mốc 7 ngày cho mọi loại đơn hàng và thiết bị. | • **Free Pre-Owned:** Đổi trả/hoàn tiền trong **15 ngày** kể từ ngày giao thành công.<br>• **Brand-New & Paid Pre-Owned:** Đổi trả/hoàn tiền trong **30 ngày**.<br>• **Thiết bị không lỗi (Non-Defective):** Đổi trả trong **7 ngày** (khách chịu phí ship).<br>• **Cước tháng & Gói bổ sung (ILD/Data):** Tuyệt đối **không hoàn tiền**. | **Lỗi Fatal QA 25% (False Promise):** Tước quyền lợi 30 ngày của khách mua máy upgrade; hứa hoàn tiền gói cước viễn thông vi phạm quy định tài chính. |
| **Bảo Hành Thiết Bị (Warranty Policy)** | Bảo hành duy nhất 15 ngày cho tất cả các dòng điện thoại. | • **Free Pre-Owned & Phụ kiện:** Bảo hành **15 ngày** kể từ ngày nhận.<br>• **Brand-New & Paid Upgrade:** Bảo hành **30 ngày** kể từ ngày nhận.<br>• **Hư hỏng vật lý/ngoại quan (Cosmetic/Physical):** Bắt buộc báo trong **48 giờ** từ khi giao.<br>• **Nhãn trả hàng (Return Label):** Tối đa **7 ngày làm việc** để gửi bưu điện. | Bỏ sót mốc **48 giờ** & khung **30 ngày**: Công ty phải chịu chi phí bảo hành màn hình vỡ do khách làm rơi sau 48h, hoặc từ chối bảo hành hợp lệ của máy trả phí. |
| **Trợ Giá Thiết Bị (Device Subsidy)** | Cam kết duy trì dịch vụ 365 ngày. | • **Cam kết trợ giá thiết bị (Device Subsidy Requirement):** Đúng **180 ngày** active liên tục. | Sai lệch hợp đồng: Khách chỉ cần active 180 ngày để hoàn tất nghĩa vụ trợ giá. Báo 365 ngày gây hoang mang và phát sinh khiếu nại leo thang. |
| **Mã Chuyển Mạng Ra (Port-Out PIN)** | Mã PIN có giá trị 4 ngày (thiếu cảnh báo). | • Mã Transfer PIN có hiệu lực **4 ngày**.<br>• Cảnh báo hủy cước trợ giá nếu chưa đủ **180 ngày**.<br>• Cảnh báo mất vĩnh viễn số điện thoại nếu tài khoản bị de-enroll do non-usage. | Khách khiếu nại phí phạt hợp đồng trợ giá hoặc mất số oan do hiểu sai quy định. |
| **Chưa Sử Dụng (Non-Usage / NUC)** | Mốc 30 ngày + 15 ngày cảnh báo (Tổng 45 ngày). | • 30 ngày inactive + 15 ngày thông báo.<br>• Sau 45 ngày: Hủy tài khoản vào ngày 46, **cập nhật dữ liệu NLAD trong 1 ngày làm việc**. | Khớp tuyệt đối với quy định của FCC và quy trình cập nhật dữ liệu USAC/NLAD. |

---

## MỤC LỤC CHI TIẾT
1. [Trụ Cột 1: CPNI Account Verification & An Ninh Tài Khoản](#1-trụ-cột-1-cpni-account-verification--an-ninh-tài-khoản)
2. [Trụ Cột 2: Logistics, Fulfillment & Vận Chuyển (DCNR, LIT, RTS, Hot Rush)](#2-trụ-cột-2-logistics-fulfillment--vận-chuyển-dcnr-lit-rts-hot-rush)
3. [Trụ Cột 3: Vòng Đời Thiết Bị, Bảo Hành (15D/30D/48H), BYOD & PUK](#3-trụ-cột-3-vòng-đời-thiết-bị-bảo-hành-15d30d48h-byod--puk)
4. [Trụ Cột 4: Quản Lý Thuê Bao, MDN ($25) & Dịch Vụ Mạng (ILD/Roaming/Voicemail)](#4-trụ-cột-4-quản-lý-thuê-bao-mdn-25--dịch-vụ-mạng-ildroamingvoicemail)
5. [Trụ Cột 5: Tuân Thủ Pháp Lý & Lifeline Lifecycle (Non-Usage 45d + NLAD 1d, Recertify)](#5-trụ-cột-5-tuân-thủ-pháp-lý--lifeline-lifecycle-non-usage-45d--nlad-1d-recertify)
6. [Trụ Cột 6: Quy Trình Port-Out (PIN 4 Ngày & Cam Kết 180 Ngày Trợ Giá)](#6-trụ-cột-6-quy-trình-port-out-pin-4-ngày--cam-kết-180-ngày-trợ-giá)
7. [Trụ Cột 7: Cancellation (Tier 1 & MDM Buy-Out) & Refund Toàn Diện](#7-trụ-cột-7-cancellation-tier-1--mdm-buy-out--refund-toàn-diện)
8. [Trụ Cột 8: 8 Kịch Bản Nghiệp Vụ Sinh Tử (Hot Rush, Fraud Slamming, Loyalty, Voicemail...)](#8-trụ-cột-8-8-kịch-bản-nghiệp-vụ-sinh-tử)

---

## 1. TRỤ CỘT 1: CPNI ACCOUNT VERIFICATION & AN NINH TÀI KHOẢN

### 1.1. Quy Định CPNI Bắt Buộc (Policy_Account Verification V1.1)
Trước khi cung cấp thông tin tài khoản, CSR **Martin** bắt buộc xác minh đủ 3 yếu tố nhận diện:
- **Full Name:** First + Last Name khớp CRM. Bỏ qua Middle Name và hậu tố *Jr., Sr., II, III*.
- **Date of Birth (DOB):** Khớp chính xác 100% (`MM/DD/YYYY`).
- **Last 4 Digits of SSN (SSN4):** Khớp chính xác 100%.
- **Thông tin liên hệ bổ sung:** Thu thập Email và Callback Number (MDN hoặc số thay thế).
- **Quy tắc an ninh cập nhật:** Tuyệt đối không đính kèm ID proof vào Activity Note trên CRM (chỉ lưu Chat ID / Ticket ID).

---

## 2. TRỤ CỘT 2: LOGISTICS, FULFILLMENT & VẬN CHUYỂN (DCNR, LIT, RTS, HOT RUSH)

| Sự Cố Logistics | Nhận Diện Hệ Thống | Giải Pháp & Quy Trình CSR Thực Hiện | SLA / Phụ Trách |
| :--- | :--- | :--- | :--- |
| **DCNR (Delivered Not Received 3.1)** | Tracking báo `Delivered` nhưng khách báo mất. | • Sai địa chỉ khách điền: Khách chịu trách nhiệm, tặng SIM BYOD.<br>• FedEx giao sai: Làm thủ tục đổi máy mới.<br>• Trộm cắp tại cửa: Cấp Voucher hoặc đổi máy theo chính sách.<br>• **Bắt buộc tạo NUC Ticket** chống hủy tài khoản vì non-usage. | Assignee: Khang Tran (`khangtran@hthcomm.com`). Xử lý: **24–48h**. |
| **LIT (Lost In Transit 2.1)** | Tracking ngừng cập nhật > 7 ngày làm việc. | • Đơn =< $100: Suspend line, blacklist máy, tạo ticket `[Carrier] Claim under $100`.<br>• Đơn > $100: Ghi file Courtesy, báo kênh FAQ, tạo ticket `LIT [Carrier] Claim (over) $100`. | Assignee: Khang Tran. Xử lý: **24–48h**. |
| **RTS (Return To Sender 1.1)** | Kiện hàng bị trả về do `Undeliverable / Bad Address`. | Khách bắt buộc nộp **Proof of Address (POA)** trong vòng **10 ngày calendar**. Quá 10 ngày đơn hàng tự động hủy và hoàn tiền. | Thẩm định địa chỉ: **24–48h**. |
| **Hot Rush Ticket** | Đơn VIP, khiếu nại pháp lý FCC/BBB hoặc đơn hàng trả phí chậm trễ. | Tạo ticket loại `Hot Rush - EO / CO - High Priority Fulfillment` gửi kho ưu tiên xuất hàng. | Assignee: Cuong Nguyen. Xuất kho: **24–48h**. |

---

## 3. TRỤ CỘT 3: VÒNG ĐỜI THIẾT BỊ, BẢO HÀNH (15D/30D/48H), BYOD & PUK

### 3.1. Chính Sách Bảo Hành Thiết Bị Chuẩn Xác:
- **Free Pre-Owned Phone & Phụ Kiện:** Bảo hành **15 ngày** kể từ ngày giao.
- **Brand-New & Paid Upgrade Phone:** Bảo hành **30 ngày** kể từ ngày giao.
- **Hư hỏng Ngoại Quan / Rơi Vỡ (Cosmetic/Physical Damage):** **BẮT BUỘC BÁO TRONG VÒNG 48 GIỜ** kể từ khi carrier giao hàng. Báo sau 48 giờ bị từ chối bảo hành vật lý.
- **Nhãn Trả Hàng (Return Label):** Phải được bưu điện đóng dấu gửi đi (postmarked) trong vòng **7 ngày làm việc**.

### 3.2. Quy Tắc Trợ Giá & BYOD:
- **Cam kết trợ giá thiết bị (Device Subsidy Requirement):** Khách hàng phải duy trì dịch vụ liên tục **180 ngày**.
- **Quy định đơn máy miễn phí:** Khách hàng chỉ được nhận 1 máy miễn phí mỗi 365 ngày; nếu có tài khoản trong 365 ngày qua, đơn đổi sang SIM BYOD.
- **Mã PUK:** Sai mã PIN 3 lần -> Khóa PUK. Nhập sai PUK 10 lần -> **Cháy chip SIM vĩnh viễn**.

---

## 4. TRỤ CỘT 4: QUẢN LÝ THUÊ BAO, MDN ($25) & DỊCH VỤ MẠNG (ILD/ROAMING/VOICEMAIL)

- **Đổi Số Điện Thoại (MDN Change):** Ưu tiên gói đổi số phí **$25**. Cảnh báo số tái sử dụng vẫn có thể nhận tin rác.
- **Cấm Chuyển Vùng Quốc Tế (Roaming Prohibited):** AirTalk chỉ hoạt động trong lãnh thổ Hoa Kỳ. Tuyệt đối cấm Roaming ngoài nước Mỹ.
- **Gọi Quốc Tế (ILD):** Miễn phí 80 quốc gia không giới hạn; hạn mức $10/tháng cho các nước còn lại. Gói cước Pay-As-You-Go kích hoạt rồi **không được hoàn tiền**.
- **Cài Đặt Hộp Thư Thoại (Voicemail):** Reset mã PIN về 4 số cuối của MDN trên CRM, nhấn giữ phím 1 để thiết lập.

---

## 5. TRỤ CỘT 5: TUÂN THỦ PHÁP LÝ & LIFELINE LIFECYCLE (NON-USAGE 45D + NLAD 1D, RECERTIFY)

- **Quy Tắc Non-Usage 30 + 15 = 45 Ngày:**
  - Ngày 1–30: Không phát sinh cước -> Hệ thống gửi cảnh báo.
  - Ngày 31–45: 15 ngày ân hạn để thực hiện cuộc gọi, gửi SMS, bật data hoặc bấm NUC trên App/IVR.
  - **Ngày 46:** Tự động hủy tài khoản (de-enroll), cập nhật cơ sở dữ liệu quốc gia **NLAD trong vòng 1 ngày làm việc**.
- **Tái Xác Thực Hàng Năm (Recertify):** Khách bị USAC de-enroll do trượt recertify được cấp **Re-apply Link cá nhân hóa** để kết nối lại nhanh chóng.

---

## 6. TRỤ CỘT 6: QUY TRÌNH PORT-OUT (PIN 4 NGÀY & CAM KẾT 180 NGÀY TRỢ GIÁ)

- **Điều Kiện OCS:** Thuộc 1 trong 4 trạng thái: `Active`, `Hotlined`, `Barred`, `Expired`.
- **Mã Transfer PIN:** Có hiệu lực **4 ngày calendar**.
- **Cảnh Báo Sống Còn Cho Khách:**
  1. Hủy bỏ vĩnh viễn quyền lợi trợ cấp Lifeline miễn phí hàng tháng của AirTalk.
  2. Nếu chưa hoàn thành **180 ngày cam kết duy trì dịch vụ** cho thiết bị trợ giá, khách sẽ bị áp dụng phí phạt vi phạm cam kết (*non-commitment hardware fees*).
  3. Nếu số bị hủy do non-usage, số điện thoại sẽ bị thu hồi và không thể chuyển mạng.
- **Phân Nhánh Carrier:** AT&T hủy sau 48h; MVNO-C có 15 ngày để Port-in và Retention hủy cuối tháng.

---

## 7. TRỤ CỘT 7: CANCELLATION (TIER 1 & MDM BUY-OUT) & REFUND TOÀN DIỆN

### 7.1. Chính Sách Hoàn Tiền Chuẩn (Refund Policy):
- **Free Pre-Owned:** Hoàn tiền/đổi trả trong **15 ngày** kể từ ngày giao.
- **Brand-New & Paid Pre-Owned:** Hoàn tiền/đổi trả trong **30 ngày** kể từ ngày giao.
- **Thiết Bị Không Lỗi (Non-Defective):** Hoàn tiền trong **7 ngày** (khách tự chịu phí vận chuyển trả hàng).
- **Cước Thuê Bao Tháng, Data Top-up & Gói ILD:** **Tuyệt đối không hoàn tiền**.
- **Lỗi Stripe Authorization Hold:** Khoản tiền Pending tự động nhả sau **7–10 ngày làm việc**, không có khoản credit refund.

### 7.2. Hủy Dịch Vụ & Mua Lại Máy MDM (Buy-Out):
- Tier 1 probe lý do, thực hiện retention và risk disclosure. Nếu khách kiên quyết -> Tạo Cancellation Ticket chuyển **Tier 2**.
- Thiết bị cài đặt phần mềm quản lý **MDM** phải thanh toán khoản mua lại (*Remaining Device Subsidy*) nếu muốn mở khóa trước thời hạn cam kết 180 ngày.

---

## 8. TRỤ CỘT 8: 8 KỊCH BẢN NGHIỆP VỤ SINH TỬ

1. **Hot Rush Ticket & Out of Stock:** Đơn chuẩn 3–5 ngày. Nếu trễ hoặc hết hàng: Đổi dòng tương đương hoặc tạo Hot Rush Ticket xuất hàng trong 24–48h (Assignee: Cuong Nguyen).
2. **Lost/Stolen & Khóa Blacklist IMEI:** Báo mất trong 48h đối với giao nhận ban đầu. Khóa an ninh ngay lập tức, chặn IMEI trên National Blacklist.
3. **Return to Sender (RTS):** Bưu kiện bị trả về yêu cầu nộp Proof of Address (POA) trong **10 ngày calendar**; quá hạn tự hủy đơn.
4. **Hủy Port-Out & Winback Retention:** Giải thích rủi ro mất trợ cấp và phí vi phạm cam kết 180 ngày. Hủy mã PIN 4 ngày và khôi phục active.
5. **Giả Mạo Đại Lý & Cướp Lợi Ích Lifeline (Slamming):** AirTalk không có đại lý tận nhà. Gửi đơn Reverse Transfer Consent và báo Hotline USAC: **1-800-234-9473**.
6. **Loyalty Program & Thưởng Giới Thiệu:** Active nhận 2 điểm/tháng (Tribal nhận 5 điểm/tháng). Giới thiệu bạn bè nhận $5–$25 (bạn nhận $5–$10), đổi Data hoặc Amazon e-Gift Card.
7. **Quy Định Nghiêm Ngặt Về Roaming & ILD:** Cấm Roaming ngoài nước Mỹ. Gọi quốc tế ILD yêu cầu mua thêm và không hoàn tiền sau kích hoạt.
8. **Hộp Thư Thoại (Voicemail Setup):** Reset mật khẩu về 4 số cuối của MDN trên CRM, nhấn giữ phím 1 để kích hoạt.
