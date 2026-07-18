import time
import requests

# Configuration placeholders
URL = "https://checkton.online/backend/spam"
API_KEY = "lNcECAAqUrqgESlGnQeP31eFyL-S9jcHmmfDGT9zEFs"
DEVICE_ID = "and_cd9e459ea708a948d5c2f5a6ca8838cfb1d974786d47d54c43295be4-ffba-4b9c-aa03-400d683351d8"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
    "X-Api-Key": API_KEY
}

payload = {
    "device_id": DEVICE_ID,
    "server": "global"
}

print("Starting request loop. Press Ctrl+C to stop.")

while True:
    try:
        response = requests.post(URL, json=payload, headers=headers)
        print(f"Status Code: {response.status_code} | Response: {response.text}")
        
        # Pause to prevent resource exhaustion and respect rate limits
        time.sleep(1.0)
    except requests.exceptions.RequestException as e:
        print(f"Network error encountered: {e}")
        time.sleep(2.0)
