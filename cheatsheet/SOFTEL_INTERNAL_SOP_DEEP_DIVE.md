# INTERNAL OPERATIONS & SOP TECHNICAL SPECIFICATION
**AirTalk Wireless & TAG Mobile - Lifeline / ACP / MVNO Infrastructure**
*Document ID: SOP-INT-DIVE-2026-V3 | Classification: Technical Operations Manual*
*Authorized Role: Tier 1 Customer Support Representative (Agent: Martin)*
*Source Material: Reconciliation of 57 Audited Standard Operating Procedures, Regulatory Policies, and Internal Training Matrices*

---

## Document Overview & Regulatory Scope

This technical specification provides an exhaustive, granular breakdown of all operational systems, regulatory compliance frameworks, and back-office procedures governing customer service operations at Softel Solutions. All processes described are audited against Federal Communications Commission (FCC) statutory mandates, Universal Service Administrative Company (USAC) Universal Service Fund rules, National Lifeline Accountability Database (NLAD) synchronization protocols, and merchant payment security standards.

---

## Table of Contents
1. [Subsystem 1: CPNI Authentication, SIM Port-Protection & Identity Theft Security](#subsystem-1)
2. [Subsystem 2: Anti-Spam Investigation & Evasion Mitigation Architecture](#subsystem-2)
3. [Subsystem 3: Port-Out Management & Inter-Carrier Provisioning Lifecycle](#subsystem-3)
4. [Subsystem 4: Product Refund Architecture & Stripe Merchant Settlement](#subsystem-4)
5. [Subsystem 5: Subscription Cancellation, Tier 1 Retention & MDM Buy-Out Protocols](#subsystem-5)
6. [Subsystem 6: Logistics Disruption, Freight Carrier Claims & Priority Fulfillment](#subsystem-6)
7. [Subsystem 7: Hardware RMA Protocols, Warranty Governance & BYOD Rules](#subsystem-7)
8. [Subsystem 8: Statutory Lifeline Compliance, 45-Day Non-Usage & Recertification](#subsystem-8)
9. [Subsystem 9: Application Adjudication, NLAD TRIV Resolution & Order Modifications](#subsystem-9)
10. [Subsystem 10: Cellular Provisioning, MDN Migration, Voicemail & ILD/Roaming Routing](#subsystem-10)

---

<a name="subsystem-1"></a>
## 1. Subsystem 1: CPNI Authentication, SIM Port-Protection & Identity Theft Security

### 1.1 Regulatory & Statutory Basis
- `Policy_Account Verification_AirTalk & TAG_V1.1.pdf` (Effective Oct 3, 2026)
- `SOP_Account Verification Handling_AirTalk & TAG_V1.2.pdf`
- `Identity Theft.pdf` (Version 1 - Change log May 2025)
- `SIM Port Protection - CSR only.pdf`
- Statutory Authority: 47 U.S.C. § 222; FCC 47 CFR §§ 64.2001–64.2011 (Customer Proprietary Network Information).

### 1.2 Multi-Factor Authentication Architecture
Prior to acknowledging account existence, balances, order numbers, shipping tracking, or executing line modifications, representatives must authenticate the subscriber using three mandatory identity tokens:

```mermaid
flowchart TD
    InboundSession["Inbound Customer Interaction"] --> PromptTokens["Prompt Mandatory Verification Tokens<br/>1. Full Legal Name<br/>2. Date of Birth (MM/DD/YYYY)<br/>3. Last 4 Digits of SSN"]
    
    PromptTokens --> EvalTokens{"Token Match Against CRM"}
    
    EvalTokens -- "3 of 3 Match Exactly" --> AuthPassed["Authentication Successful<br/>Capture Secondary Contact Info:<br/>- Callback Number (MDN)<br/>- Verified Email Address"]
    AuthPassed --> OpenService["Permit Full Account Servicing"]
    
    EvalTokens -- "Discrepancy (Attempt 1 or 2)" --> Reprompt["Inform of Data Discrepancy<br/>Strict Prohibition:<br/>- Never confirm partial guesses<br/>- Never reveal stored CRM data"]
    Reprompt --> PromptTokens
    
    EvalTokens -- "Discrepancy (Attempt 3+)" --> Lockout["Terminal Failure: Deploy :atw-cpni-fail<br/>Restrict Session to General Policies Only<br/>Direct Subscriber to Secure Government ID Upload"]
```

#### Detailed Field Matching Specifications:
- **Full Legal Name:** First Name and Last Name must match the CRM subscriber record identically. Middle names are non-blocking. Suffixes (*Jr., Sr., II, III, IV*) are disregarded if First and Last names match. Name punctuation discrepancies (hyphens, apostrophes) are treated as matches.
- **Date of Birth (DOB):** Must match the recorded date in `MM/DD/YYYY` format with zero character variance.
- **SSN Last 4 Digits:** Must match the recorded 4-digit token synchronized with USAC/NLAD records.

### 1.3 SIM Port-Protection Security Daemon
- **Automated Lockout Trigger:** If a customer or representative enters incorrect authentication tokens **3 consecutive times** during replacement SIM provisioning or Transfer PIN generation, the OCS provisioning daemon automatically trips the `SIM Port-Protection` lock.
- **CRM Indicator:** The Activity Log generates the system entry: `SIM - Port Protection turned on / Locks Account`.
- **Remediation Protocol:** Representatives are barred from manual override. The subscriber must log into their authenticated web portal (`Account > My SIM > SIM - Port Unlock`) to perform self-service cryptographic unlocking.

### 1.4 Identity Theft & Federal Privacy Data Hygiene
- **Mandatory CRM Note Hygiene:** Pursuant to federal data protection standards (May 2025 change log), representatives are **strictly barred from attaching or pasting subscriber identity documents (passports, driver's licenses, SSN cards) into CRM Activity Notes**.
- **Audit-Compliant Note Standard:** Representatives must record only the encrypted **Ticket ID** or **Chat Session ID** containing the uploaded document asset.

---

<a name="subsystem-2"></a>
## 2. Subsystem 2: Anti-Spam Investigation & Evasion Mitigation Architecture

### 2.1 Regulatory & Statutory Basis
- `SOP_Spam Handling_AirTalk & TAG_V2.2_Active_2026-10-26.docx` (Active Oct 26, 2026 - 1,130 Paragraphs)
- `SMS Spamming.pdf`, `SOP Spamming.drawio`

### 2.2 Forensic Investigation Workflow

```mermaid
flowchart TD
    SpamAlert["Account Flagged: Automated Spam / Bulk SMS Pattern"] --> ApplyHotline["OCS Applies Mandatory Hotline ID<br/>Block New SIM Order Engine on CRM & App<br/>Maintain Unrestricted 911 Emergency Access"]
    
    ApplyHotline --> ForensicReview["Representative Performs Forensic Usage Audit<br/>Review 30 Days of Outbound Call/SMS Records:<br/>- High-frequency burst patterns<br/>- Identical SMS payload across unique destinations<br/>- Sequential non-random dialing"]
    
    ForensicReview --> CXInquiry{"Subscriber Contacts Support"}
    
    CXInquiry --> DetectEvasion{"Is Subscriber Attempting Evasion?<br/>- Requesting MDN Change<br/>- Demanding New SIM Order<br/>- Requesting Port-In / Port-Out<br/>- Filing False Lost/Stolen or DCNR Claim"}
    
    DetectEvasion -- "Yes (Evasion Flag)" --> HaltEvasion["Deploy :atw-spam-evasion<br/>Halt All Ancillary Provisioning Immediately<br/>Demand Immediate Identity Re-verification"]
    
    DetectEvasion -- "No" --> RequestID["Explain Security Verification Mandate<br/>Require Proof Submission:<br/>1. High-resolution photo holding ID adjacent to face<br/>2. If ambiguous: 5-10s video reciting Name & DOB"]
    
    HaltEvasion --> RequestID
    RequestID --> SubmitFraud["Attach Assets to CRM Fraud Ticket<br/>Escalate to Fraud & Compliance Review Team<br/>SLA: 24 to 48 Business Hours"]
```

### 2.3 Regulatory Evasion Countermeasures
Subscribers operating bulk commercial messaging or phishing rings frequently deploy evasion tactics upon hotline activation. Under SOP V2.2, the following rules are mandatory:
1. **Total Freeze on Line Alterations:** While flagged for spam investigation, no representative may process an MDN change, issue a replacement SIM, approve an equipment claim, or process a port-in.
2. **Block Caller Governance:** Representatives may not toggle the Block Caller switch autonomously. Any request to block callers must be escalated as a High Priority ticket via the internal FAQ channel to the Supervisor / Tech Lead team.
3. **Emergency Access (911):** 911 dialing capabilities must remain active across all hotline states. If technical system constraints impede 911 routing, the representative must immediately engage IT network operations to ensure dial-out compliance.

---

<a name="subsystem-3"></a>
## 3. Subsystem 3: Port-Out Management & Inter-Carrier Provisioning Lifecycle

### 3.1 Regulatory & Statutory Basis
- `SOP_Port-Out_AirTalk & TAG_V2.1_Active_2026-10-19.docx` (506 Paragraphs)
- `Porting Guideline.pdf`, `Cancel Port-Out - MVNO-C.png`, `PO-GEN-P001` through `P005.png`
- Statutory Authority: FCC Wireless Local Number Portability (LNP) Rules (47 CFR § 52.35).

### 3.2 OCS Line Qualification & Delivery Architecture

```mermaid
sequenceDiagram
    autonumber
    actor CX as Subscriber
    actor CSR as Support Agent (Martin)
    participant OCS as OCS / CRM Provisioning Engine
    participant Carrier as Gaining Carrier Network

    CX->>CSR: Requests Account Number & Port-Out Transfer PIN
    CSR->>OCS: Perform 3-Factor CPNI Verification
    OCS-->>CSR: Verification Confirmed
    CSR->>OCS: Query OCS Line Status
    
    alt Status NOT in (Active, Hotlined, Barred, Expired)
        CSR->>CX: Port-Out Rejected: Status ineligible. Account must be in serviceable state.
    else Status Qualified
        CSR->>CX: Advise on 180-Day Hardware Subsidy Lock & Loss of Federal Benefit
        CSR->>CX: Designate Single Transmission Route (SMS with ICCID OR Verified Email)
        Note over CSR,OCS: Transmission strictly restricted to ONE channel to avoid dual-code generation
        CSR->>OCS: Execute Transfer PIN Generation (Expires in exactly 4 Calendar Days)
        OCS-->>CX: Transfer PIN Dispatched via Designated Route
        CSR->>OCS: Create Cancellation CRM Ticket
        
        alt Underlying Network is AT&T
            Note over OCS: Account automatically cancelled 48 hours post-ticket creation
        else Underlying Network is MVNO-C
            Note over OCS: 15-day transfer window granted - Retention sweeps cancel at month-end
        end
        
        Carrier->>OCS: Inter-Carrier Port Request Transmitted
        OCS-->>Carrier: Line Released & Number Ported
    end
```

### 3.3 Critical Operational Rules
- **4-Day PIN Lifespan:** The Transfer PIN generated by the OCS engine has an immutable lifespan of **4 calendar days (96 hours)**. Stating 30 days is a fatal QA compliance error.
- **180-Day Subsidy Disclosure:** Representatives must explicitly warn subscribers that transferring their line prior to completing **180 consecutive active days** of service triggers hardware non-commitment penalties and prevents device unlocking.
- **Account Number Designation:** The account number is the subscriber's 10-digit MDN or internal Enrollment ID.

---

<a name="subsystem-4"></a>
## 4. Subsystem 4: Product Refund Architecture & Stripe Merchant Settlement

### 4.1 Regulatory & Statutory Basis
- `SOP_Refund_AirTalk&TAG_V3.1_Active_2026-10-20.pdf` (84 pages)
- `Refund-case-studies.pdf` (19 slides)

### 4.2 Comprehensive 7-Product Evaluation Engine

```mermaid
flowchart TD
    RefundReq["Customer Demands Refund"] --> CheckStripe{"Stripe Merchant Status"}

    CheckStripe -- "Authorized / Pending" --> HoldProtocol["Stripe Authorization Hold Protocol:<br/>- Transaction is an uncaptured temporary hold<br/>- Funds automatically drop within 7-10 business days<br/>- No financial credit or refund ticket generated"]

    CheckStripe -- "Completed / Succeeded" --> EvaluateCategory{"Product Line Evaluation"}

    EvaluateCategory -- "1. Plan Upgrade / Renewal" --> CheckPlan{"Requested <= 48 Hours AND Unprovisioned?"}
    CheckPlan -- "Yes" --> ApproveRefund["Submit Accounting Refund Ticket"]
    CheckPlan -- "No" --> DenyRefund["Strictly Non-Refundable"]

    EvaluateCategory -- "2. Data Top-Up / Roaming" --> CheckData{"Any MB Data Consumed?"}
    CheckData -- "Yes" --> DenyRefund
    CheckData -- "No (Purchased in Error)" --> TL_Data["Supervisor de-provisions package -> Approved"]

    EvaluateCategory -- "3. Hardware Device" --> HandsetTier{"Handset Classification"}
    HandsetTier -- "Free Lifeline Phone" --> FreeTime{"Delivered <= 15 Calendar Days?"}
    FreeTime -- "Yes" --> ApproveRefund
    FreeTime -- "No" --> DenyRefund
    HandsetTier -- "Brand-New / Paid Upgrade" --> PaidTime{"Delivered <= 30 Calendar Days?"}
    PaidTime -- "Yes" --> ApproveRefund
    PaidTime -- "No" --> DenyRefund
    HandsetTier -- "Non-Defective Return" --> NonDefTime{"Delivered <= 7 Calendar Days?"}
    NonDefTime -- "Yes" --> CustomerFreight["Approved: Customer pays return shipping"]
    NonDefTime -- "No" --> DenyRefund

    EvaluateCategory -- "4. Express Shipping" --> CheckShip{"Warehouse Fulfillment Scanned?"}
    CheckShip -- "Not Scanned" --> ApproveRefund
    CheckShip -- "Scanned / Shipped" --> DenyRefund

    EvaluateCategory -- "5. Accessories" --> AccCheck{"Returned <= 7 Days in Original Box?"}
    AccCheck -- "Yes" --> ApproveRefund
    AccCheck -- "No" --> DenyRefund

    ApproveRefund --> SettleProcessing["Accounting Processes Settlement:<br/>- Original Payment Method: 3 to 5 business days<br/>- Service Voucher: Instant credit (AirTalk Only)"]
```

---

<a name="subsystem-5"></a>
## 5. Subsystem 5: Subscription Cancellation, Tier 1 Retention & MDM Buy-Out Protocols

### 5.1 Regulatory & Statutory Basis
- `Policy_Cancellation_AirTalk & TAG_V1.1.pdf` (Effective Aug 28, 2026)
- `SOP_Cancellation Handling - Tier 1_AirTalk & TAG_V1.1.pdf`
- `SOP_Cancellation Handling - Tier 2_AirTalk & TAG_V1.0.pdf`
- `Retention.pdf`

### 5.2 Tier 1 Cancellation & Escalation Protocol

```mermaid
flowchart TD
    CancelIntent["Subscriber Demands Service Cancellation"] --> VerifyAuth["Execute Mandatory CPNI Authentication"]
    VerifyAuth --> ProbeRoot["Diagnostic Discovery & Root Cause Probing:<br/>- Inadequate cellular coverage<br/>- Defective hardware<br/>- Competitor migration<br/>- Relocation / Address change"]
    
    ProbeRoot --> RetentionPitch["Deploy Tailored Retention Mitigation:<br/>- Network reprovisioning / APN update<br/>- Technical troubleshooting / SIM swap<br/>- Emphasize loss of federal Lifeline subsidy<br/>- Warn of permanent forfeiture of MDN"]
    
    RetentionPitch --> CXOutcome{"Subscriber Decision"}
    
    CXOutcome -- "Accepts Retention Offer" --> ApplyRemedy["Apply Agreed Remedy (Troubleshoot / Upgrade SIM)<br/>Document Outcome in CRM & Close Interaction"]
    
    CXOutcome -- "Insists on Cancellation" --> Tier1Barrier["Strict Prohibition:<br/>Tier 1 Representatives CANNOT cancel lines on OCS"]
    
    Tier1Barrier --> CheckMDM{"Is Handset Governed by Active MDM Subsidy?"}
    
    CheckMDM -- "Yes (< 180 Days Active)" --> MDMStatement["Issue MDM Buy-Out Statement:<br/>Inform customer device remains locked until<br/>remaining hardware subsidy balance is remitted"]
    CheckMDM -- "No (>= 180 Days or BYOD)" --> EscalateTier2["Generate CRM Ticket: 'Cancellation Request - Tier 1 Escalated'<br/>Transfer File to Tier 2 Cancellation Review Team"]
    MDMStatement --> EscalateTier2
```

---

<a name="subsystem-6"></a>
## 6. Subsystem 6: Logistics Disruption, Freight Carrier Claims & Priority Fulfillment

### 6.1 Regulatory & Statutory Basis
- `Delivered Not Received (DCNR) V3.1.pdf` (52 pages)
- `Lost In Transit (LIT) V2.1.pdf` (11 pages)
- `Return to Sender (RTS) V1.1.pdf`
- `Hot Rush Ticket.pdf`

### 6.2 Logistics Claim Matrix & Routing Architecture

```mermaid
flowchart TD
    FreightDispute["Freight Disruption Reported"] --> CarrierTrace{"Tracking Scan State"}

    CarrierTrace -- "Marked Delivered (Customer claims not received)" --> DCNR_Path["DCNR V3.1 Investigation"]
    DCNR_Path --> CheckAddr{"Address Matches Approved Application?"}
    CheckAddr -- "Customer Error" --> CX_Liable["Customer Liability: No free hardware replacement.<br/>Provide free replacement BYOD SIM."]
    CheckAddr -- "Address Confirmed" --> DCNR_Process["Carrier GPS Scan & Proof of Delivery Audit<br/>Assignee: Khang Tran (khangtran@hthcomm.com)<br/>Mandatory: Create NUC Ticket to protect account<br/>Resolution SLA: 24 to 48 business hours"]

    CarrierTrace -- "Stalled > 7 Business Days Past SLA" --> LIT_Path["Lost In Transit V2.1 Protocol"]
    LIT_Path --> CheckVal{"Declared Hardware Value"}
    CheckVal -- "<= $100.00" --> LIT_Low["Suspend Line + Blacklist IMEI<br/>Create Accounting Ticket: '[Carrier] Claim under $100'<br/>Assignee: Khang Tran<br/>File NUC Ticket"]
    CheckVal -- "> $100.00" --> LIT_High["Suspend Line + Blacklist IMEI<br/>Record Entry in Courtesy Sheet: 'LIT - free replacement request'<br/>Escalate via FAQ Channel<br/>Create Accounting Ticket: 'LIT [Carrier] Claim (over) $100'"]

    CarrierTrace -- "Returned by Carrier" --> RTS_Path["Return To Sender V1.1 Protocol"]
    RTS_Path --> RTS_Hold["Request Proof of Address (POA)<br/>10 Calendar Days Submission Window<br/>If POA Verified: Warehouse Re-ships via FedEx<br/>If POA Missing at Day 10: Automatic Cancellation & Refund"]

    CarrierTrace -- "FCC/BBB Complaint or Paid Priority" --> Rush_Path["Hot Rush Fulfillment Protocol"]
    Rush_Path --> Rush_Exec["Create Ticket: 'Hot Rush - EO / CO - High Priority Fulfillment'<br/>Assignee: Cuong Nguyen<br/>Target Warehouse Dispatch: 24 to 48 Hours<br/>Exclusion: Partner Store Orders (PAT Prefix) Ineligible"]
```

---

<a name="subsystem-7"></a>
## 7. Subsystem 7: Hardware RMA Protocols, Warranty Governance & BYOD Rules

### 7.1 Regulatory & Statutory Basis
- `ETC Handset_ Accessory Replacement Policy_During EBB_ACP_Final.pdf`
- `Warranty replacement V1.2.pdf` (33 pages)
- `REPLACEMENTS V1.1.pdf` (22 pages)
- `Bring Your Own Device.pdf` (Change log 27/03/2026)
- `PUK Code.pdf` (10 pages)

### 7.2 Hardware RMA & Troubleshooting Ladder

```mermaid
flowchart TD
    HandsetFault["Hardware Defect Reported"] --> FailureClass{"Nature of Defect"}

    FailureClass -- "Physical, Cosmetic, Water or Screen Damage" --> CosmeticCheck{"Reported <= 48 Hours of Delivery?"}
    CosmeticCheck -- "Yes" --> RMA_Cosmetic["Approve Transit Damage RMA<br/>Issue Prepaid Return Label (7 Business Days Validity)"]
    CosmeticCheck -- "No" --> Deny_Cosmetic["Claim Rejected: Post-delivery physical damage.<br/>Direct customer to paid upgrade replacement."]

    FailureClass -- "Internal Electronic / Operating System Defect" --> WarrantyTier{"Device Warranty Category"}
    WarrantyTier -- "Free Lifeline Handset" --> CheckFree["Evaluate Against 15 Calendar Days Window"]
    WarrantyTier -- "Brand-New / Paid Upgrade" --> CheckPaid["Evaluate Against 30 Calendar Days Window"]

    CheckFree & CheckPaid -- "Within Window" --> MandatoryTroubleshoot["Execute Required Troubleshooting:<br/>1. Hard power cycle & battery pull<br/>2. SIM card re-seat & gold contact clean<br/>3. Network APN profile reset<br/>4. Factory data reset (if OS responsive)"]

    MandatoryTroubleshoot --> TroubleshootResult{"Defect Cleared?"}
    TroubleshootResult -- "Yes" --> DocumentSuccess["Document Diagnostic Steps in CRM & Close Ticket"]
    TroubleshootResult -- "No" --> ReplacementLadder["Deploy Replacement Ladder:<br/>1. Offer Paid Upgrade Replacement<br/>2. Issue Standard Warranty RMA Replacement<br/>3. Offer Free BYOD SIM Replacement"]

    CheckFree & CheckPaid -- "Outside Window" --> ExpiredWarranty["Warranty Expired: Offer discounted replacement handset"]
```

### 7.3 Critical Hardware Governance Mandates
1. **The 365-Day Free Handset Rule:** Subscribers who have received a government-subsidized device within the preceding **365 calendar days** are ineligible for additional free devices. Applications are automatically converted to **BYOD (SIM-only)**.
2. **PUK Lockout Protocol:** 3 incorrect PIN entries lock the SIM card; 10 incorrect PUK entries permanently destroy the SIM microchip, requiring an order for replacement hardware.

---

<a name="subsystem-8"></a>
## 8. Subsystem 8: Statutory Lifeline Compliance, 45-Day Non-Usage & Recertification

### 8.1 Regulatory & Statutory Basis
- `Non-usage Guideline - ver 1.1.pdf` (SNU project & IVR Consent updates)
- `[AirTalk] Assistance Guideline for De-enroll CXs Due to Fail Recertify.pdf` (July 16 update)
- Statutory Authority: FCC 47 CFR § 54.405(e)(3); 47 CFR § 54.407(c)(2).

### 8.2 The 45-Day Non-Usage Statutory State Machine

```mermaid
stateDiagram-v2
    [*] --> ActiveState: Subscriber Enrolled in National Lifeline Registry
    
    ActiveState --> ActiveState: Billable Usage Recorded (Outbound Call / SMS / Mobile Data / NUC)
    ActiveState --> WarningState: 30 Consecutive Days with Zero Recorded Billable Events
    
    state WarningState {
        [*] --> IssueNotice: Automated Cure Notice Issued (Day 30)
        IssueNotice --> AwaitingCure: 15-Day Cure Window Commences (Days 31 to 45)
    }
    
    WarningState --> ActiveState: Subscriber Cures Non-Usage:<br/>- Places Outbound Call<br/>- Sends Outbound SMS<br/>- Consumes Mobile Data off Wi-Fi<br/>- Executes NUC Consent via App or IVR
    
    WarningState --> DeEnrolledState: Day 45 Concludes with Zero Curing Events
    
    state DeEnrolledState {
        [*] --> ServiceTermination: Day 46 - Immediate Network Disconnection
        ServiceTermination --> NLAD_Sync: Transmit De-enrollment to NLAD within 1 Business Day
        NLAD_Sync --> NumberQuarantine: MDN Assigned to Quarantine Pool
    }
```

### 8.3 Recertification Failure Remediation
When a subscriber is flagged for de-enrollment due to failure to complete annual USAC recertification:
1. AirTalk does not perform immediate abrupt disconnection; the line remains provisionally active.
2. The representative generates an authenticated **Re-apply Link** directly through the CRM console.
3. If MDN retention is required, the representative must submit a priority IT provisioning ticket to prevent recycling before re-enrollment approval.

---

<a name="subsystem-9"></a>
## 9. Subsystem 9: Application Adjudication, NLAD TRIV Resolution & Order Modifications

### 9.1 Regulatory & Statutory Basis
- `Application Assistance Guideline.pdf`
- `Application-Assistance-Guideline-Case-Studies.pdf`
- `Customer Orders Change.pdf`

### 9.2 Adjudication & Identity Resolution Workflows
1. **Applications Exceeding 30 Days:** Application files pending identity proof or address validation for more than 30 days are automatically expired by the national registry. Representatives must guide subscribers through initiating a fresh application.
2. **NLAD TRIV (Third-Party Identity Verification) Failures:**
   - Occurs when subscriber PII cannot be validated against credit bureaus or government identity registries.
   - Representatives must escalate the application to the **Review Team** and instruct the subscriber to upload a clear government photo ID and proof of Social Security Number via the secure portal.
3. **Tribal Eligibility Reclassification:** If an applicant is rejected for Tribal enhanced subsidies due to geographic boundary verification failures, representatives must reclassify the application to standard Lifeline, assign standard shipping, and swap device allocation to approved baseline models (e.g., model **A56**).

---

<a name="subsystem-10"></a>
## 10. Subsystem 10: Cellular Provisioning, MDN Migration, Voicemail & ILD/Roaming Routing

### 10.1 Network Operations & Provisioning Flowchart

```mermaid
flowchart TD
    NetReq["Network Provisioning / Service Request"] --> ServiceType{"Service Category"}

    ServiceType -- "Mobile Number Change (MDN)" --> MDN_Flow["MDN Change SOP V1.2:<br/>- Disclose number recycling and persistent spam risks<br/>- Assess standard $25.00 MDN change fee<br/>- Waive fee only upon verified police harassment report<br/>- Instruct customer: Power off phone for 3 minutes"]

    ServiceType -- "eSIM Profile Setup" --> eSIM_Flow["eSIM Provisioning Protocol:<br/>- Verify device connected to Wi-Fi<br/>- Transmit authenticated QR profile voucher<br/>- Troubleshoot 'Unable to Continue': Wipe corrupt profile and reset APN"]

    ServiceType -- "International Calling (ILD)" --> ILD_Flow["ILD Operating Standard:<br/>- 80 countries unlimited dialing<br/>- $10/month cap on non-unlimited destinations<br/>- Auto-suspended after 6-12 months inactivity to prevent toll fraud<br/>- Representative may re-enable via CRM upon subscriber request"]

    ServiceType -- "International Roaming" --> Roam_Flow["Roaming Governance Policy:<br/>- AirTalk / TAG strictly limited to domestic US towers<br/>- International roaming barred technically and contractually"]

    ServiceType -- "Voicemail Provisioning" --> VM_Flow["Voicemail Standard Protocol:<br/>- Reset mailbox PIN to last 4 digits of MDN on CRM<br/>- Customer presses and holds key '1' on dialer to initialize"]
```

---

## 11. Operational SLA & Responsibility Assignment Directory

| Operational Domain | Governing SOP | SLA Commitment | Assignee / Department | Escalation Route |
| :--- | :--- | :--- | :--- | :--- |
| **Logistics Freight Claims (DCNR/LIT)** | DCNR V3.1 / LIT V2.1 | 24 to 48 Business Hours | Khang Tran (`khangtran@hthcomm.com`) | Logistics Supervisor / FAQ Channel |
| **Hot Rush Priority Fulfillment** | Hot Rush SOP | 24 to 48 Hours to Dispatch | Cuong Nguyen (Fulfillment Lead) | Executive Office Escalations |
| **Hardware Cosmetic Defect Notice** | Handset Policy V1.2 | Strictly <= 48 Hours | Tier 1 CSR (Martin) | Reverse Logistics Lead |
| **Hardware RMA Label Validity** | Handset Policy V1.2 | 7 Business Days Postmark | Warehouse Receiving Team | Accounting Inventory Desk |
| **Port-Out PIN Validity** | Port-Out SOP V2.1 | 4 Calendar Days (96h) | Automated OCS Provisioning | Tech Support / OCS Engineering |
| **Stripe Authorization Release** | Refund SOP V3.1 | 7 to 10 Business Days | Customer Issuing Bank | Merchant Services Accounting |
| **Approved Refund Settlement** | Refund SOP V3.1 | 3 to 5 Business Days | Accounting / Treasury Desk | Finance Lead |
| **Lifeline Non-Usage De-enrollment** | Non-Usage SOP V1.1 | Day 46 Disconnect / 1bd NLAD | Compliance / USAC Daemon | Legal & Regulatory Desk |
| **Cancellation Ticket Review** | Cancellation V1.1 | 24 to 48 Business Hours | Tier 2 Cancellation Review Team | Retention Management |
