Zoom Recording Downloader: Setup and Usage Documentation
1. Prerequisites
Before running the script, ensure you have the following:

Python 3.x installed on your machine.

pip installed to manage Python packages.

A Zoom OAuth App set up with the necessary scopes and credentials.

A .env file to securely store your Zoom API credentials.

2. Creating and Configuring the Zoom OAuth App
To interact with the Zoom API, you must first create an OAuth app and configure it with the necessary scopes.

Steps to Create a Zoom OAuth App:
Go to the Zoom Developer Dashboard:

Navigate to Zoom App Marketplace.

Log in to your Zoom account.

Click on Develop > Build App.

Create a New OAuth App:

Select OAuth from the app types.

Fill out the necessary details for your app:

App Name: Choose a name for your app (e.g., "Zoom Recording Downloader").

App Description: Provide a brief description of your app (optional).

OAuth Redirect URL: You can use a localhost URL during development (e.g., http://localhost:8080).

Category: Select the category that best describes your app.

Get Your App Credentials:

Once your app is created, navigate to the App Credentials section to retrieve the following details:

Client ID

Client Secret

Account ID

Configure OAuth Scopes:

Under OAuth Scopes, add the following scopes:

account:read - Allows the app to access account-level information.

user:read - Provides access to user details within the account.

meeting:read - Access to read meeting details, including recordings.

recording:read - Allows access to recordings for meetings.

report:read (optional) - Provides access to meeting reports.

Save Your App Settings.

3. Setting Up Your Python Script
Step 1: Install Required Python Packages
Install the necessary Python packages using pip:

bash
Copy
Edit
pip install requests python-dotenv
Step 2: Create a .env File for Zoom API Credentials
Create a .env file in the same directory as your script. The file will securely store your Zoom credentials:

.env File Contents:
plaintext
Copy
Edit
ZOOM_ACCOUNT_ID=your_zoom_account_id
ZOOM_CLIENT_ID=your_zoom_client_id
ZOOM_CLIENT_SECRET=your_zoom_client_secret
Replace your_zoom_account_id, your_zoom_client_id, and your_zoom_client_secret with the credentials obtained from the Zoom Developer Dashboard.

4. Running the Script
Step 1: Download the Script
Download the Python script from the repository or create it in your own editor using the guidelines provided.

Step 2: Set Up the .env File
Create a .env file in the same directory as the script and insert your Zoom API credentials as described earlier.

Step 3: Install Dependencies
Install the required Python packages by running the following command:

bash
Copy
Edit
pip install requests python-dotenv
Step 4: Run the Script
Once everything is set up, run the script by executing:

bash
Copy
Edit
python zoom_recording_downloader.py
Expected Output:
The script will download all Zoom recordings from the specified date range into a folder called zoom_recordings. The recordings are organized by year, month, and meeting details.

5. Troubleshooting
Invalid OAuth Token: Ensure that your OAuth token is valid. If expired, you'll need to regenerate it by authenticating through Zoom's OAuth flow.

Scope Errors: Ensure you have added the correct scopes in your Zoom OAuth app settings as specified in this documentation.

Download Errors: If a download fails, the script will skip that file and continue with the next one.

6. Notes
OAuth App Credentials:
Client ID: The unique identifier for your app.

Client Secret: The secret key for authenticating your app.

Account ID: The Zoom account ID tied to the app.

These credentials are stored in the .env file to keep them secure. Never commit the .env file to any public repository.

7. License and Attribution
This project is open-source, and you are free to use, modify, and distribute it under the terms of the MIT License.

8. Contribution
Feel free to fork this repository and submit a pull request if you have improvements, bug fixes, or new features you'd like to contribute.

