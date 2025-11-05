# INCIDENT RESPONSE FINAL REPORT

## 1. Incident Overview

| Field | Detail |
| :--- | :--- |
| **Incident Title** | [e.g., Phishing Campaign Leading to Credential Compromise] |
| **IR ID Number** | [e.g., IR-2025-01-23-0042] |
| **Date/Time Detected** | [YYYY-MM-DD HH:MM UTC] |
| **Date/Time Closed** | [YYYY-MM-DD HH:MM UTC] |
| **Security Analyst Lead** | [(Toluwanimi Oladele-Ajose)] |
| **Severity (Initial/Final)** | [e.g., P2/P3 - High/Medium] |
| **Incident Type** | [e.g., Credential Compromise, Malware Outbreak, Data Exfiltration] |
| **NIST Phase Closed In** | [e.g., 4. Post-Incident Activity] |

## 2. Executive Summary

A brief, non-technical summary (2-3 paragraphs) detailing what happened, the business impact, the estimated duration of the compromise, and the final resolution.
* *Example: On [Date], the SOC detected unauthorized access to a user mailbox originating from [Country/IP]. Immediate containment measures limited the breach to one user account. No evidence of data exfiltration was found, and the incident was resolved by enforcing a password reset and MFA re-enrollment.*

## 3. Incident Timeline

A detailed chronological list of events, actions taken, and the analyst responsible.

| Timestamp (UTC) | Event Description | Action Taken/Analyst |
| :--- | :--- | :--- |
| 2025-11-05 09:30 | Alert triggered: 'Unusual Geo-Location Login'. | Analyst T.A. assigned case. |
| 2025-11-05 09:45 | Confirmed login from unverified IP (178.x.x.x). | Account disabled via Active Directory. |
| 2025-11-05 10:30 | Mailbox audit confirms 5 suspicious emails sent. | Phishing emails deleted; email cache cleared. |
| 2025-11-05 12:00 | User password reset and MFA re-enrolled. | Account re-enabled. Case closed. |

## 4. Technical Details and Analysis

### 4.1. Systems Affected
* Number of Endpoints: [e.g., 1]
* System Names/IPs: [e.g., WORKSTATION-TOLU-001]
* Data Classification Involved: [e.g., PII, Confidential]

### 4.2. Indicators of Compromise (IOCs)
| IOC Type | Value | Threat Intel Verdict (e.g., VT) |
| :--- | :--- | :--- |
| IP Address | 178.x.x.x | Known VPN Egress / Malware C2 |
| URL/Domain | malicious-login-page.com | PHISHING |
| File Hash (SHA256) | [N/A or hash value] | CLEAN / MALICIOUS |

### 4.3. Root Cause Analysis
[e.g., The root cause was a lack of MFA enforcement on the affected cloud service, combined with a successful spear-phishing attack.]

## 5. Containment, Eradication, and Recovery (CER) Actions

| Action | Tool Used | Result |
| :--- | :--- | :--- |
| **Containment** | Blocked inbound connection from [IP] | Successful, no further external access observed. |
| **Eradication** | Forced Password Reset/MFA | Successful, invalidating attacker's session. |
| **Recovery** | Endpoint full-scan (Cortex XDR) | Clean bill of health for the affected system. |

## 6. Post-Incident Activity & Lessons Learned

### 6.1. Remediation and Recommendations
* **Immediate Fix:** [e.g., Enforce MFA requirement for all external access.]
* **Long-Term Improvement:** [e.g., Conduct a review of all legacy VPN accounts for weak passwords.]
* **Detection Improvement:** [e.g., Create a new SIEM rule to alert on more than 3 failed logins in 5 minutes.]

### 6.2. Sign-Off
Report Prepared By: __________________________
Reviewer: __________________________
