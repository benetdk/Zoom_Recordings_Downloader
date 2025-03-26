# Zoom Downloader Setup and Usage Guide

## Overview
This guide explains how to set up, configure, and run the Zoom Downloader script to download all organization-wide Zoom recordings, organizing them by year, month, date, and user.

---

## 1. Setting Up the Zoom App
To use the script, you need to set up a Zoom App with the required API permissions.

### Step 1: Create a Zoom App
1. Log in to the [Zoom App Marketplace](https://marketplace.zoom.us/).
2. Click on **Develop** > **Build App**.
3. Select **Server-to-Server OAuth** and click **Create**.
4. Provide a name for your app and click **Create**.

### Step 2: Get API Credentials
1. Navigate to the **App Credentials** section.
2. Copy the **Client ID**, **Client Secret**, and **Account ID**.

### Step 3: Set Permissions
1. Go to the **Scopes** tab.
2. Add the following permissions:
   - `recording:read:admin` (to read all recordings in the organization)
3. Click **Save & Continue**.
4. Activate your app by clicking **Activate**.

---

## 2. Installing Dependencies
Ensure you have Python installed (preferably Python 3.9 or later). Then, install the required dependencies:

```sh
pip install requests
```

---

## 3. Configuring the Script
Edit the script to include your Zoom API credentials:

```python
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
ACCOUNT_ID = "your_account_id"
```

---

## 4. Modifying the Date Range
By default, the script fetches all recordings from January 1, 2020, to today. You can modify this by changing the following lines in the script:

```python
start_date = "2020-01-01"  # Change this to your desired start date
today = datetime.today().strftime("%Y-%m-%d")
end_date = today  # Change this to your desired end date
```

For example, to download recordings from 2023 only:

```python
start_date = "2023-01-01"
end_date = "2023-12-31"
```

---

## 5. Running the Script
Run the script using:

```sh
python Zoom_Downloader.py
```

The script will:
- Authenticate with Zoom API.
- Fetch all recordings within the date range.
- Organize downloads into folders structured as: `zoom_recordings/YYYY/MM/YYYY-MM-DD_HH-MM_user_topic/`.
- Save recordings in the appropriate folders.

---

## 6. Troubleshooting
- **Authentication errors**: Ensure your API credentials are correct and your Zoom app is activated.
- **No recordings found**: Check if the date range is correct and if recordings exist.
- **Download issues**: Ensure you have internet access and the API is not rate-limited.

For further assistance, refer to the [Zoom API documentation](https://marketplace.zoom.us/docs/api-reference/introduction/).

