# AI Receptionist

## Overview

AI Receptionist is an AI-powered calling system that reminds participants about events, meetings, or appointments. It automates the process of sending voice reminders using AI-generated speech and integrates with scheduling systems to ensure timely notifications.

## Features

- **Automated Calls**: AI-powered voice calls to remind users about their upcoming events.
- **Natural Language Processing (NLP)**: Converts text reminders into human-like speech.
- **Integration with Calendar APIs**: Syncs with Google Calendar, Outlook, or custom scheduling systems.
- **Customizable Messages**: Personalize messages based on user preferences.
- **Multi-language Support**: Supports multiple languages for global accessibility.
- **Call Status Tracking**: Logs call success/failure and retries if needed.

## Technologies Used

- **Programming Language**: Python
- **Speech Synthesis**: Google Text-to-Speech (gTTS), Amazon Polly, or OpenAI TTS
- **Telephony API**: Twilio API or an equivalent VoIP service
- **Database**: PostgreSQL / Firebase / MongoDB (for storing user details and schedules)
- **Framework**: Flask / FastAPI for backend services
- **Scheduling**: Celery / Cron Jobs for task automation

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- pip package manager
- Twilio API account (if using Twilio for calling)
- Google Cloud / AWS account (for TTS services, if required)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AI-Receptionist.git
   cd AI-Receptionist
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   Create a `.env` file and add the required API keys and configurations.
   ```ini
   TWILIO_ACCOUNT_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_phone
   GOOGLE_API_KEY=your_google_api_key
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## Usage

- Add participants and their contact details.
- Schedule reminders via an integrated calendar or manual input.
- The AI Receptionist will make automated calls at scheduled times.
- Monitor call status through logs or a dashboard.

## API Endpoints

| Method | Endpoint           | Description              |
| ------ | ------------------ | ------------------------ |
| POST   | /schedule\_call    | Schedule a reminder call |
| GET    | /calls             | Retrieve call logs       |
| DELETE | /cancel\_call/{id} | Cancel a scheduled call  |

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to your branch and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any queries, reach out to indupriya0565\@gmail.com or create an issue on GitHub.

