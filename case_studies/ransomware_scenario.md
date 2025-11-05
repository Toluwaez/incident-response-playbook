# Case Study: Ransomware Attack (LockBit Variant Simulation)

**Date:** March 2025
**Role:** SOC Analyst Tier 2/Incident Handler
**Incident Type:** Ransomware
**Tools Used:** Splunk, Cortex XDR, Tenable.io, Network Access Control (NAC)

## 1. Detection & Triage

### 1.1 Initial Alert
* **Source:** **Cortex XDR** triggered a "High Severity" alert for "Mass File Encryption" originating from a service account on the file server (`FS-PROD-01`).
* **SIEM:** **Splunk** simultaneously alerted on a high volume of outbound connections to a non-standard port and external IP (`203.x.x.x`) associated with the C2 beacon.

### 1.2 Analysis
* **Initial Access:** Investigation revealed the ransomware entered via an unpatched RDP vulnerability on an old QA server (`QA-SERVER-05`).
* **Movement:** The attacker used the QA server to compromise a less-privileged service account, then exploited a weak credential to move laterally to the production file server (`FS-PROD-01`).
* **IOCs:** File hash (`e928...`), C2 IP, and ransom note text were collected and recorded.

## 2. Containment, Eradication, & Recovery

### 2.1 Containment
* **Immediate Isolation:** Used **Cortex XDR** to isolate the QA server and the file server (`FS-PROD-01`) from the network immediately.
* **Network Segmentation:** Temporarily disabled SMB (Server Message Block) shares and blocked all outbound traffic to the C2 IP (`203.x.x.x`) globally at the perimeter.
* **Access Revocation:** Disabled the compromised service account across the entire domain.

### 2.2 Eradication
* **Forensics:** Took a full memory dump and disk image of the compromised servers for the Forensic Team.
* **Cleanup:** Identified and removed the ransomware executable and dropped files.
* **Patching:** Identified the specific RDP vulnerability (**CVE-2023-XXXX**) and applied the patch to all vulnerable servers identified via **Tenable.io**.

### 2.3 Recovery
* **Verification:** Verified that the latest backups were clean and unencrypted.
* **Restoration:** Restored critical data on `FS-PROD-01` from the last known-good backup.
* **Re-enablement:** Re-enabled the clean, patched, and verified servers back into the production network environment.

## 3. Post-Incident Activities

* **Executive Review:** Presented a high-level summary of the incident and the response actions to executive management.
* **Security Control Enhancement:** Implemented mandatory network segmentation rules to prevent lateral movement between QA and Production environments in the future.
* **Documentation:** Created a full **Chain of Custody** log for the seized server images and closed the incident.
