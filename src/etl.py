import os
import requests
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Public threat intelligence feed (IP blocklist)
THREAT_FEED_URL = "https://feodotracker.abuse.ch/downloads/ipblocklist.txt"

def fetch_threat_feed():
    print("📡 Fetching IP feed...")
    response = requests.get(THREAT_FEED_URL)
    response.raise_for_status()

    # Parse IP addresses, skipping comments and empty lines
    ips = []
    for line in response.text.splitlines():
        if line.strip() and not line.startswith("#"):
            ips.append(line.strip())
    print(f"✅ Fetched {len(ips)} IPs.")
    return ips

def insert_into_supabase(ips):
    print("☁️ Inserting into Supabase...")

    data = [{"ip_address": ip} for ip in ips]
    batch_size = 500  # Supabase API batch limit

    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        res = supabase.table("threat_indicators").insert(batch).execute()
        if res.data:
            print(f"Inserted {len(batch)} rows ✅")
        else:
            print(f"⚠️ Batch insert failed: {res}")

def main():
    try:
        ips = fetch_threat_feed()
        insert_into_supabase(ips)
        print("🎯 ETL completed successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
