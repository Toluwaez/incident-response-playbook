# Case Study: Targeted Phishing Response Leading to Credential Harvesting

**Date:** June 2025
**Role:** SOC Analyst Tier 2
**Incident Type:** Phishing/Credential Harvesting
**Tools Used:** Microsoft Defender for Endpoint, Defender for Office 365, Splunk, VirusTotal

## 1. Detection & Triage

### 1.1 Initial Alert
* **Source:** A high-priority alert was triggered in **Defender for Office 365** indicating a suspicious login from a non-US IP address shortly after a user reported a "strange email."
* **Triage:** Initial review showed a successful login from **Nigeria (154.x.x.x)** immediately following the user clicking a link in an email disguised as a "SharePoint Document Link."

### 1.2 Analysis
* **IOCs:** Extracted the malicious URL (`onedrive-verification-login.com`) and the originating IP address.
* **Threat Intel:** Verified the URL on **VirusTotal**; it was flagged as a known credential harvesting site.
* **Impact Assessment:** Checked email logs; 3 internal emails were sent from the compromised account containing the phishing link to other high-value targets (VPs in Finance).

## 2. Containment, Eradication, & Recovery

### 2.1 Containment
* **Account Action:** Immediately ran a PowerShell command to **revoke all existing session tokens** and **force a global password reset** for the affected user.
* **Email Gateway:** Blocked the malicious sender domain and the harvested URL at the perimeter firewall/proxy.
* **Internal Spread:** Used **Defender for Office 365** to **purge (delete)** the 3 internal malicious emails from all recipient inboxes.

### 2.2 Eradication
* **Endpoint Scan:** Ran a full scan on the user's endpoint using **Defender for Endpoint** to ensure no keylogger or malicious software was installed. Scan came back clean.
* **MFA Re-enrollment:** Requested the user to **re-enroll their MFA token** to invalidate any potential session tokens the attacker might have captured.

### 2.3 Recovery
* **User Interview:** Conducted a brief interview with the user to understand the exact link clicked and the process of entering their credentials.
* **Monitoring:** Set up **Splunk alerts** to watch for any further authentication attempts from the attacker's IP and any unusual mailbox activity for the next 48 hours.

## 3. Post-Incident Activities

* **Lessons Learned:** The attack succeeded due to the user's lack of training on identifying URL spoofing.
* **Recommendation:** Implemented an organization-wide simulated phishing campaign using a similar template within 1 week.
* **Documentation:** Completed and submitted the **Incident Report Template (.docx)** and attached the email headers to the **Evidence Collection Form (.xlsx)**.
