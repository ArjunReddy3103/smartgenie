import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
import os

# Define the scope of the permissions
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]   

# Load credentials from the JSON key file
key_path = os.getenv("GOOGLE_SHEETS_CREDENTIALS_PATH")
creds = ServiceAccountCredentials.from_json_keyfile_name(key_path, scope)
# Authorize the client
client = gspread.authorize(creds)

# Name of your Google Sheet
SHEET_NAME = 'Chatbot Logs'  # Make sure your sheet has this exact name
sheet = client.open(SHEET_NAME).sheet1

def log_prompt(prompt: str, user_ip: str = 'N/A'):
    """
    Appends a user prompt with timestamp and optional IP to the Google Sheet.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sheet.append_row([timestamp, prompt, user_ip])
