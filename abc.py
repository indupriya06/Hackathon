import datetime
import pywhatkit as kit
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from twilio.rest import Client

# Twilio Credentials (Replace with your actual credentials)
TWILIO_ACCOUNT_SID = "ACbfc29f706a7037e2079708895c8f9f82"
TWILIO_AUTH_TOKEN = "ae37fcb19f744fc41b0921286f23175e"
TWILIO_PHONE_NUMBER = "+18566363789"
TO_PHONE_NUMBER = "+919100266979"  # Change to recipient's number

# Google Calendar API Credentials
SERVICE_ACCOUNT_FILE = "credentials.json"
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_calendar_service():
    """Initialize Google Calendar API service."""
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build("calendar", "v3", credentials=creds)


def list_events():
    """Fetch upcoming events from Google Calendar."""
    service = get_calendar_service()
    now = datetime.datetime.utcnow().isoformat() + "Z"

    events_result = service.events().list(
        calendarId="veeramachinenilikhitha2@gmail.com",
        timeMin=now,
        maxResults=1,  # Fetch the next event
        singleEvents=True,
        orderBy="startTime",
    ).execute()

    events = events_result.get("items", [])

    if not events:
        print("⚠️ No upcoming events found.")
        return None

    event = events[0]  # Get the first event
    event_name = event["summary"]
    start_time = event["start"].get("dateTime", event["start"].get("date"))

    return event_name, start_time


def send_sms(message):
    """Send an SMS using Twilio."""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        sms = client.messages.create(
            body=message, from_=TWILIO_PHONE_NUMBER, to=TO_PHONE_NUMBER
        )
        print(f"✅ SMS sent successfully! SID: {sms.sid}")
    except Exception as e:
        print(f"❌ ERROR: {e}")


def send_whatsapp_message(phone_number, message, hour, minute):
    """Send a WhatsApp message using pywhatkit."""
    try:
        kit.sendwhatmsg(phone_number, message, hour, minute)
        print(f"✅ WhatsApp message scheduled for {phone_number} at {hour}:{minute}!")
    except Exception as e:
        print(f"❌ ERROR: {e}")


if __name__ == "__main__":
    print("🚀 Fetching event from Google Calendar...")
    event_details = list_events()

    if event_details:
        event_name, event_time = event_details
        event_hour, event_minute = map(int, event_time[11:16].split(":"))  # Extract time

        reminder_message = f"📅 Reminder: {event_name} is scheduled at {event_time}."

        # Sending SMS
        send_sms(reminder_message)

        # Sending WhatsApp message
        send_whatsapp_message(TO_PHONE_NUMBER, reminder_message, event_hour, event_minute - 1)  # 1 min before event
