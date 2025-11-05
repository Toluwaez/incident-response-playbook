# 📧 Phishing Incident Response Playbook

## 1. Detection
- Alert triggered in Microsoft Defender for Office 365.
- User reports suspicious email with unknown sender.
- SIEM rule: "Multiple failed logins followed by successful login from unusual IP".

## 2. Analysis
- Extract Indicators of Compromise (IOCs): sender domain, URLs, attachments, and IP addresses.
- Review email header for spoofing signs.
- Query threat intelligence platforms (Recorded Future, VirusTotal) for indicators.
- Check user authentication logs in Splunk for anomalies.

## 3. Containment
- Quarantine the reported email in all mailboxes.
- Block sender’s domain and IP address in the email gateway.
- Temporarily disable compromised user accounts.

## 4. Eradication
- Remove all malicious emails from mailboxes using EAC or PowerShell.
- Delete related malicious files or scripts from endpoints.
- Revoke and reissue any affected credentials.

## 5. Recovery
- Reset passwords for affected users.
- Restore normal operations and monitor for repeated attempts.
- Validate email security configurations (SPF, DKIM, DMARC).

## 6. Post-Incident
- Conduct phishing awareness refresher training.
- Update detection rules and SIEM correlation logic.
- Document findings and submit a post-incident report.
