# extract_logs_splunk.py
# Purpose: Simulates querying the Splunk REST API to retrieve logs during an incident.
# Note: This is a simplified example. A real implementation would require proper error handling, 
# job polling, and secure credential management (e.g., using environment variables or a secret vault).

import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # Disable SSL warnings for testing

# --- Configuration ---
# This would be replaced with the actual Splunk details and API token
SPLUNK_URL = "https://splunk.corp.example.com:8089"
SPLUNK_API_TOKEN = "Bearer YOUR_SECURE_API_TOKEN_HERE" 

# Example search query for an incident (e.g., failed logins for a specific user)
SEARCH_QUERY = "search index=authentication source=win:security 'Failed Login' user=Toluwanimi | table _time, host, user, status"

# --- API Endpoints ---
SEARCH_ENDPOINT = f"{SPLUNK_URL}/services/search/jobs"
RESULTS_ENDPOINT_BASE = f"{SPLUNK_URL}/services/search/jobs"

HEADERS = {
    "Authorization": SPLUNK_API_TOKEN,
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_search_job(query):
    """Submits the search query to Splunk and creates a search job."""
    print(f"[*] Submitting search: {query}...")
    try:
        response = requests.post(
            SEARCH_ENDPOINT,
            headers=HEADERS,
            data={"search": query, "output_mode": "json"},
            verify=False  # Set to True and provide cert path in production
        )
        response.raise_for_status()
        
        job_data = response.json()
        sid = job_data.get('sid')
        if sid:
            print(f"[+] Search Job created with SID: {sid}")
            return sid
        else:
            print("[-] Error: Could not retrieve SID from response.")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Error submitting search job: {e}")
        return None

def get_job_results(sid):
    """Retrieves the results of a finished search job."""
    
    # In a real scenario, you would poll the job status (isDone) first.
    # For this example, we assume the job is small and finishes quickly.
    
    results_url = f"{RESULTS_ENDPOINT_BASE}/{sid}/results?output_mode=json"
    print("[*] Retrieving results...")
    
    try:
        response = requests.get(results_url, headers=HEADERS, verify=False)
        response.raise_for_status()
        
        results = response.json()
        
        if 'results' in results:
            print(f"[+] Retrieved {len(results['results'])} log entries.")
            return results['results']
        else:
            print("[-] No results found.")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Error retrieving results: {e}")
        return []

if __name__ == "__main__":
    job_sid = create_search_job(SEARCH_QUERY)
    
    if job_sid:
        log_data = get_job_results(job_sid)
        
        if log_data:
            # Output results to the console or a file
            print("\n--- Log Extraction Results (First 5) ---")
            for entry in log_data[:5]:
                print(json.dumps(entry, indent=2))
        else:
            print("\n[!] Script finished, but no log data was collected.")
