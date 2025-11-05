import requests

# Simple script to analyze indicators (IOCs) using VirusTotal API
API_KEY = "YOUR_VIRUSTOTAL_API_KEY"
IOC_LIST = ["maliciousdomain.com", "45.77.89.12", "suspiciousfile.exe"]

def analyze_ioc(ioc):
    url = f"https://www.virustotal.com/api/v3/search?query={ioc}"
    headers = {"x-apikey": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"IOC: {ioc}\nAnalysis Summary: {data.get('data', 'No results')}\n")
    else:
        print(f"Error analyzing {ioc}: {response.status_code}")

if __name__ == "__main__":
    for ioc in IOC_LIST:
        analyze_ioc(ioc)
