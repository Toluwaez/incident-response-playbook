# Insider Threat Response Playbook

## 1. Detection
* **DLP Alert:** Data Loss Prevention (DLP) system alerts on a large volume of sensitive data being copied to a USB drive or uploaded to a personal cloud storage service (e.g., Dropbox, OneDrive).
* **UEBA:** User and Entity Behavior Analytics (UEBA) platform flags "abnormal" behavior (e.g., employee accessing files outside of their job role, logging in at unusual hours).
* **HR/Manager Report:** A manager reports suspicious behavior or an employee resigns abruptly and begins accessing high-value data.

## 2. Analysis
* **Classification:** Determine if the threat is **Malicious** (intentional data theft, sabotage) or **Unintentional** (accidental data leak, policy violation).
* **Data Staging:** Identify *what* data was accessed/exfiltrated and where it was staged (e.g., compressed and encrypted folder on a local drive).
* **Motive Assessment:** Liaise with HR/Legal to understand the employee's context (e.g., disciplinary action, job change, dissatisfaction). *Note: The SOC Analyst focuses on technical data; HR/Legal drives the motive assessment.*
* **Technical Audit:** Review all communication logs (email, chat) and file access logs for the past 90 days related to the individual.

## 3. Containment
* **Access Restriction:** **Immediately revoke** the user's access to all sensitive systems and databases (using a pre-approved, coordinated lockout plan).
* **Physical Security:** If the threat is Malicious, coordinate with physical security to revoke building access and monitor the individual's presence.
* **Device Isolation:** Block network access for the user's primary workstation to prevent further data transfer.

## 4. Eradication
* **Device Seizure:** Preserve the user's corporate device (laptop, phone) following a strict chain of custody for forensic analysis (managed by Legal/Forensics team).
* **Data Integrity:** Verify the integrity of systems and data that the insider had access to (e.g., ensure no backdoors or logic bombs were planted).
* **Account Deletion:** If the employee has been terminated, fully delete the account after legal holds are in place.

## 5. Recovery
* **System Validation:** Restore any system settings or configuration files that were intentionally altered by the insider.
* **Policy Review:** Review and tighten permissions across all systems that were accessed by the insider, applying the Principle of Least Privilege.
* **Communication:** Coordinate with internal communications to address any potential internal or external perception damage.

## 6. Post-Incident
* **Legal/HR Handover:** Fully transfer all forensic evidence, technical logs, and incident reports to the Legal and HR teams for potential disciplinary or legal action.
* **Control Review:** Implement stronger technical controls like enhanced DLP rules, stricter endpoint management, and more granular UEBA monitoring.
* **Lessons Learned:** Document the full response and any necessary changes to onboarding/offboarding processes.
