import pywhatkit as kit

# Ensure the number is in the correct format
phone_number = input("Enter the phone number (include country code, e.g., +1234567890): ").strip()
message = input("Enter your message: ")
hour = int(input("Enter the hour (24-hour format): "))
minute = int(input("Enter the minute: "))

# Validate the phone number format
if not phone_number.startswith("+") or not phone_number[1:].isdigit():
    print("Error: Invalid phone number format! Make sure to use + followed by the country code and number.")
else:
    # Send the WhatsApp message
    kit.sendwhatmsg(phone_number, message, hour, minute)
    print(f"Message scheduled successfully for {phone_number} at {hour}:{minute}!")
