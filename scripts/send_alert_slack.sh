#!/bin/bash
# send_alert_slack.sh
# Purpose: Sends a structured incident notification to a specified Slack channel via webhook.

# --- Configuration ---
# Replace with a real Slack incoming webhook URL for your testing environment
WEBHOOK_URL="https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

# Variables for the alert message
SEVERITY="CRITICAL"
INCIDENT_ID="IR-2025-042"
ALERT_TITLE="Malware Detected on Executive Endpoint"
AFFECTED_HOST="EXECUTIVE-LAPTOP-1"
ANALYST_URL="https://splunk.corp.example.com/app/search/incident?id=042" # Link to your SIEM/IR system

# Construct the JSON payload for the Slack message
SLACK_PAYLOAD=$(cat <<EOF
{
    "attachments": [
        {
            "color": "#ff0000",
            "pretext": "*${SEVERITY} Incident Detected!*",
            "title": "${INCIDENT_ID}: ${ALERT_TITLE}",
            "title_link": "${ANALYST_URL}",
            "fields": [
                {
                    "title": "Affected Host",
                    "value": "${AFFECTED_HOST}",
                    "short": true
                },
                {
                    "title": "Severity",
                    "value": "${SEVERITY}",
                    "short": true
                }
            ],
            "footer": "SOC Automation via Bash",
            "ts": $(date +%s)
        }
    ]
}
EOF
)

# Send the POST request to the Slack Webhook URL
curl -X POST -H 'Content-type: application/json' \
    --data "$SLACK_PAYLOAD" \
    "$WEBHOOK_URL"

# Check the exit status of the curl command
if [ $? -eq 0 ]; then
    echo "Slack alert successfully sent for ${INCIDENT_ID}."
else
    echo "ERROR: Failed to send Slack alert for ${INCIDENT_ID}."
fi
