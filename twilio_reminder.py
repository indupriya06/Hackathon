from twilio.rest import Client
print("Script is running!")
# Twilio credentials (Replace with your actual credentials)
TWILIO_ACCOUNT_SID = "ACbfc29f706a7037e2079708895c8f9f82"
TWILIO_AUTH_TOKEN = "ae37fcb19f744fc41b0921286f23175e"
TWILIO_PHONE_NUMBER = "+1 856 636 3789"
TO_PHONE_NUMBER = "+919100266979"  # Replace with your number

def send_sms():
    """Send SMS using Twilio"""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body="Hello! This is a test message from AI Receptionist.",
            from_=TWILIO_PHONE_NUMBER,
            to=TO_PHONE_NUMBER
        )
        print(f"✅ SMS sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"❌ ERROR: {e}")

# Run the function
send_sms()
