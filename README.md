# Incident Response Playbook (SOC Analyst)

This repository documents my approach to identifying, analyzing, containing, eradicating, and recovering from cybersecurity incidents. It reflects my workflow as a SOC Analyst handling real-world scenarios in a Security Operations Center.

---

## Purpose
To demonstrate how I apply the NIST Incident Response Framework and standard SOC procedures when responding to various security incidents.

---

## Framework Reference
**NIST SP 800-61r2**: Computer Security Incident Handling Guide

Phases:
1. **Preparation**
2. **Detection & Analysis**
3. **Containment, Eradication, & Recovery**
4. **Post-Incident Activity**

---

## Repository Overview

| Folder | Description |
|--------|--------------|
| [`incident_playbooks/`](incident_playbooks/) | Step-by-step guides for responding to different types of incidents |
| [`templates/`](templates/)| Reusable forms and report templates |
| [`scripts/`](scripts/) | Example automation or log analysis scripts |
| [`case_studies/`](case_studies/) | Simulated incidents showing end-to-end response workflow |

---

## Example: Phishing Incident Response

1. **Detection:** Alert received from email gateway or user report.  
2. **Analysis:** Extract IOCs (URLs, domains, IPs) and check against threat intel feeds.  
3. **Containment:** Block sender domain and quarantine suspicious emails.  
4. **Eradication:** Remove affected messages and reset compromised credentials.  
5. **Recovery:** Validate systems, review logs, and monitor for recurring activity.  
6. **Post-Incident:** Document lessons learned and update detection rules.

---

## Tools I Use
- **SIEM:** Splunk / Microsoft Sentinel  
- **Threat Intel:** Recorded Future, VirusTotal  
- **Endpoint:** Cortex XDR, Defender for Endpoint  
- **Vulnerability Mgmt:** Tenable.io  
- **Automation:** Python, PowerShell, Slack webhooks  

---

## Author
**Toluwanimi Oladele-Ajose**  
Security Operations & Threat Analyst  
[LinkedIn](https://www.linkedin.com/in/toluwanimi-oladele-ajose/) • [GitHub](https://github.com/Toluwaez/)
