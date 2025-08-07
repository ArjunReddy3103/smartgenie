import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
load_dotenv()
import os

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

key_path = os.getenv("GOOGLE_SHEETS_CREDENTIALS_PATH")
creds = ServiceAccountCredentials.from_json_keyfile_name(key_path, scope)
client = gspread.authorize(creds)

SHEET_NAME = 'Chatbot Logs'
sheet = client.open(SHEET_NAME).sheet1

IST = timezone(timedelta(hours=5, minutes=30))

def log_prompt(prompt: str, bot_reply: str = '', user_ip: str = 'N/A', user_id: str = 'Anonymous'):
    """
    Logs the prompt, bot reply, IP, and user ID with IST timestamp to the Google Sheet.
    """
    timestamp = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S')
    sheet.append_row([timestamp, prompt, bot_reply, user_ip, user_id])
