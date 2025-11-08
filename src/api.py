import os
from fastapi import FastAPI
from dotenv import load_dotenv
from supabase import create_client, Client

# --- Load environment variables ---
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# --- Initialize Supabase client ---
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI(title="Threat Intelligence API")

@app.get("/")
def root():
    return {"message": "Threat Intelligence API is running"}

@app.get("/check")
def check_ip(ip: str):
    """Check if an IP exists in the threat_indicators table."""
    res = supabase.table("threat_indicators").select("ip_address").eq("ip_address", ip).execute()

    if res.data and len(res.data) > 0:
        return {"ip": ip, "malicious": True, "details": res.data}
    else:
        return {"ip": ip, "malicious": False}
