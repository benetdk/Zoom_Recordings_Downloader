import requests
import os
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Cargar variables de entorno desde credentials.env
load_dotenv("credentials.env")

# Zoom API credentials
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
ACCOUNT_ID = os.getenv("ACCOUNT_ID")
BASE_URL = "https://api.zoom.us/v2"
TOKEN_URL = "https://zoom.us/oauth/token"

# Obtener token OAuth
def get_access_token():
    auth = (CLIENT_ID, CLIENT_SECRET)
    data = {"grant_type": "account_credentials", "account_id": ACCOUNT_ID}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(TOKEN_URL, auth=auth, headers=headers, data=data)
    response.raise_for_status()
    return response.json().get("access_token")

# Obtener grabaciones para un mes
def get_recordings_for_month(start_date, end_date):
    headers = {"Authorization": f"Bearer {get_access_token()}"}
    recordings = []
    page_number = 1

    while True:
        response = requests.get(
            f"{BASE_URL}/accounts/me/recordings",
            headers=headers,
            params={"from": start_date, "to": end_date, "page_size": 300, "page_number": page_number}
        )
        if response.status_code == 429:
            print("Rate limit reached. Retrying after delay...")
            time.sleep(60)
            continue

        response.raise_for_status()
        data = response.json()

        if "meetings" in data:
            recordings.extend(data["meetings"])

        if not data.get("next_page_token"):
            break
        page_number += 1

    return recordings

# Descargar grabaciones
def download_recordings(start_date, end_date):
    recordings = get_recordings_for_month(start_date, end_date)
    base_download_dir = "./zoom_recordings"
    os.makedirs(base_download_dir, exist_ok=True)

    for meeting in recordings:
        meeting_id = meeting["id"]
        host_email = meeting["host_email"]
        topic = meeting.get("topic", "Unknown_Topic").replace(" ", "_")
        start_time = datetime.strptime(meeting["start_time"], "%Y-%m-%dT%H:%M:%SZ")
        year = start_time.strftime("%Y")
        month = start_time.strftime("%m")
        folder_name = f"{start_time.strftime('%Y-%m-%d_%H-%M')}_{host_email}_{topic}"
        year_month_dir = os.path.join(base_download_dir, year, month)
        meeting_dir = os.path.join(year_month_dir, folder_name)
        os.makedirs(meeting_dir, exist_ok=True)

        for file in meeting.get("recording_files", []):
            download_url = file["download_url"]
            file_type = file["file_extension"]
            file_name = f"{meeting_id}_{file['id']}.{file_type}"
            file_path = os.path.join(meeting_dir, file_name)

            with requests.get(download_url, headers={"Authorization": f"Bearer {get_access_token()}"}, stream=True) as r:
                if r.status_code == 429:
                    print("Rate limit reached during download. Retrying after delay...")
                    time.sleep(60)
                    r = requests.get(download_url, headers={"Authorization": f"Bearer {get_access_token()}"}, stream=True)
                r.raise_for_status()
                with open(file_path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"Downloaded: {file_path}")

# Procesar cada mes en el rango de fechas
def download_for_date_range(start_date, end_date):
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

    while current_date <= end_date_obj:
        next_month = current_date + timedelta(days=32)
        next_month = next_month.replace(day=1)
        month_end = next_month - timedelta(days=1)
        
        month_start = current_date.strftime("%Y-%m-%d")
        month_end_str = month_end.strftime("%Y-%m-%d")

        print(f"Downloading recordings for: {month_start} to {month_end_str}")
        download_recordings(month_start, month_end_str)

        current_date = next_month

# Función principal
def main():
    start_date = "2025-01-01"
    end_date = "2025-12-31"
    download_for_date_range(start_date, end_date)
    print("Download process complete.")

if __name__ == "__main__":
    main()
