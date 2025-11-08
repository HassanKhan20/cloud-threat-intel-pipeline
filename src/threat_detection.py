import os
import re
from dotenv import load_dotenv
from supabase import create_client, Client

# --- Load environment variables ---
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# --- Initialize Supabase client ---
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_threat_ips():
    """Fetch all malicious IPs from the Supabase table."""
    res = supabase.table("threat_indicators").select("ip_address").execute()
    if not res.data:
        print("⚠️ No IPs found in database.")
        return []
    return [row["ip_address"] for row in res.data if row["ip_address"]]

def scan_logs(log_file, threat_ips):
    """Scan local log file for any IPs matching the threat list."""
    detected = []
    pattern = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")

    with open(log_file, "r") as f:
        for line in f:
            for ip in pattern.findall(line):
                if ip in threat_ips:
                    print(f"⚠️ Malicious IP detected: {ip}")
                    detected.append(ip)

    print(f"\n✅ Scan complete — {len(detected)} matches found.")
    return detected

def main():
    print("🧠 Loading threat intelligence data...")
    threat_ips = get_threat_ips()
    print(f"✅ Loaded {len(threat_ips)} malicious IPs from Supabase.\n")

    print("🔍 Scanning system_logs.txt for threats...")
    scan_logs("system_logs.txt", threat_ips)

if __name__ == "__main__":
    main()
