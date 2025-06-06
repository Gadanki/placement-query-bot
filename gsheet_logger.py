import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Authenticate using creds.json
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

# Open the sheets by name
query_sheet = client.open("PlacementQueryLog").sheet1
feedback_sheet = client.open("PlacementFeedbackLog").sheet1

# Function to log user queries
def log_query(user_input, category):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query_sheet.append_row([timestamp, user_input, category])

# Function to log feedback
def log_feedback(user_input, bot_response, feedback):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    feedback_sheet.append_row([timestamp, user_input, bot_response, feedback])
