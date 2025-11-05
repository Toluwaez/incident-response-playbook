# Credential Compromise Response Playbook

## 1. Detection
* **Alert:** SIEM/MFA system alerts on "Impossible Travel" (login from two distant locations in short time) or a large number of failed login attempts followed by a success.
* **Breach Notification:** External threat intel feed or public disclosure indicates corporate credentials were found on the dark web.
* **User Report:** A user reports being locked out or notices suspicious activity (e.g., emails sent from their account they didn't write).

## 2. Analysis
* **Scope:** Identify the compromised account(s) and their access level (e.g., regular user, administrator, service account).
* **Initial Access:** Determine *how* the credential was compromised (e.g., phishing, brute-force, malware keylogger, public leak).
* **Activity Review:** Examine access logs (e.g., Azure AD, Active Directory, cloud resources) for all activity by the account *since* the time of compromise. Look for:
    * File access/exfiltration.
    * New account creation or privilege escalation.
    * Mailbox rules created for forwarding.
* **IOC Collection:** Collect IP addresses and user agents used by the attacker.

## 3. Containment
* **Immediate Disable:** **Immediately disable** the compromised account in Active Directory/Identity Provider.
* **Revoke Sessions:** Force logout of all active sessions for the compromised account across all applications and endpoints.
* **Block IPs:** Block the observed attacker IP addresses at the perimeter firewall/WAF.

## 4. Eradication
* **Full Credential Reset:** Once the threat actor's activity has stopped, issue a **mandatory password reset** for the compromised account (ensuring a complex, unique password).
* **MFA Re-enrollment:** Force a re-enrollment of Multi-Factor Authentication (MFA) to invalidate any compromised session tokens or push notification approvals.
* **System Scan:** Scan the endpoint(s) the compromised user typically logs into for keyloggers or malware.

## 5. Recovery
* **Audit Trail:** Re-audit all access logs to ensure the threat actor did not leave behind any persistent access (e.g., backdoor accounts, unauthorized API keys).
* **Account Re-enablement:** Re-enable the account after a successful password reset and MFA re-enrollment.
* **Harden Policy:** Review and strengthen password and MFA policies.

## 6. Post-Incident
* **User Training:** Provide targeted training to the affected user(s) on phishing or secure credential handling.
* **Tool Review:** Verify all authentication logs are being successfully ingested by the SIEM.
* **Report:** Document the compromise, the attacker's actions, and the data accessed.
