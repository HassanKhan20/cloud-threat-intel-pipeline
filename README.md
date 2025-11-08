# cloud-threat-intel-pipeline
# ☁️ Cloud Threat Intelligence Pipeline

An end-to-end **Cybersecurity ETL and Detection API** built with **Python, Supabase, and FastAPI**, designed to fetch public threat intelligence feeds, store indicators of compromise (IOCs), and detect malicious IPs in system logs — all deployed live on the cloud.

---

## 🚀 Live Demo

**🔗 API Endpoint:** [https://threat-intel-api.onrender.com](https://threat-intel-api.onrender.com)  
**📘 Docs (Swagger UI):** [https://threat-intel-api.onrender.com/docs](https://threat-intel-api.onrender.com/docs)

---

## 🧠 Project Overview

This project simulates how cybersecurity teams collect and operationalize **Threat Intelligence Feeds** to detect and respond to potential network intrusions.

It performs three core tasks:

| Phase | Description |
|-------|--------------|
| **1. ETL (Extract → Transform → Load)** | Fetches a public threat intelligence IP feed and inserts data into a Supabase (PostgreSQL) database using the Supabase SDK. |
| **2. Detection Engine** | Scans simulated log files to flag IPs that match known malicious indicators. |
| **3. REST API** | Exposes endpoints to query whether an IP is malicious, retrieve recent logs, and check API status. |

---

## 🧩 Tech Stack

| Layer | Technologies |
|--------|--------------|
| **Backend** | Python 3.11+, FastAPI, Uvicorn |
| **Database** | Supabase (PostgreSQL) |
| **Hosting** | Render (free tier) |
| **Other Tools** | Requests, Python-Dotenv, Supabase-py |
| **Data Source** | Public Threat Intel Feed (e.g. Abuse.ch, FireHOL, etc.) |

---

## 🗂️ Project Structure

cloud-threat-intel-pipeline/
├── .env                   # Supabase credentials
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
│
├── src/
│   ├── etl.py             # Fetches threat feed and uploads to Supabase
│   ├── threat_detection.py# Scans system logs for malicious IPs
│   ├── api.py             # FastAPI endpoints (/check, /)
│   ├── system_logs.txt    # Sample log file for detection testing
│   └── __pycache__/       # Cached Python modules
│
└── supabase/
    └── threat_indicators  # Cloud table for IP intelligence



---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/HassanKhan20/cloud-threat-intel-pipeline.git
cd cloud-threat-intel-pipeline
