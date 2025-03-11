import os
import pandas as pd
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Define paths
# Define paths
path_v = r"C:\Users\Indhu\Downloads\v"  # Folder containing events.txt
path_ai = r"C:\Users\Indhu\Downloads\AI Receptionalist"  # Folder containing config.txt

# Update these paths if the files are located elsewhere
config_path = os.path.join(path_ai, "config.txt")  # Path to config.txt
events_file = os.path.join(path_v, "events.txt")  # Path to events.txt

# Load Twilio credentials from config file
config_path = os.path.join(path_ai, "config.txt")
config = {}
with open(config_path, "r") as file:
    for line in file:
        key, value = line.strip().split("=")
        config[key] = value

ACCOUNT_SID = config["ACCOUNT_SID"]
AUTH_TOKEN = config["AUTH_TOKEN"]
TWILIO_PHONE = config["TWILIO_PHONE"]
WHATSAPP_SANDBOX = config["WHATSAPP_SANDBOX"]

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Load event data from CSV
events_path = os.path.join(path_v, "events.csv")
events_df = pd.read_csv(events_path)

# Function to send SMS
def send_sms(to, message):
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=to
        )
        print(f"SMS sent to {to}: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS to {to}: {e}")

# Function to send WhatsApp message
def send_whatsapp(to, message):
    try:
        message = client.messages.create(
            body=message,
            from_=f"whatsapp:{TWILIO_PHONE}",
            to=f"whatsapp:{to}"
        )
        print(f"WhatsApp message sent to {to}: {message.sid}")
    except Exception as e:
        print(f"Failed to send WhatsApp message to {to}: {e}")

# Function to check and send reminders
def send_reminders():
    now = datetime.now()
    for index, row in events_df.iterrows():
        event_date = datetime.strptime(f"{row['Event Date']} {row['Event Time']}", "%Y-%m-%d %I:%M %p")
        reminder_time = event_date - timedelta(hours=int(row['Reminder Time'].split()[0]))
        
        if now >= reminder_time and now < event_date:
            message = f"Reminder: Your event is on {row['Event Date']} at {row['Event Time']}."
            send_sms(row["Phone Number"], message)
            send_whatsapp(row["Phone Number"], message)

# Run the reminder checker
while True:
    send_reminders()
    time.sleep(60)  # Check every minute
# Debugging: Print paths
print(f"Config path: {config_path}")
print(f"Events file path: {events_file}")

# Debugging: Print Twilio credentials
print(f"Twilio Account SID: {config['ACCOUNT_SID']}")
print(f"Twilio Auth Token: {config['AUTH_TOKEN']}")
print(f"Twilio Phone: {config['TWILIO_PHONE']}")
print(f"WhatsApp Sandbox: {config['WHATSAPP_SANDBOX']}")

# Debugging: Print events
events = parse_events(events_file)
print("Events:", events)