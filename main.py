import datetime as dt
import smtplib
import random
import os
from dotenv import load_dotenv
from email.message import EmailMessage

# Load credentials from .env
load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("MY_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")  # e.g., smtp.gmail.com

# Read quotes
with open("quotes.txt", encoding="utf-8") as quote_file:
    quotes = [line.strip() for line in quote_file if line.strip()]

# Read recipients
with open("recipients.txt", encoding="utf-8") as rec_file:
    recipients = [line.strip() for line in rec_file if line.strip()]


def send_monday_motivation():
    """Send Monday motivation email if today is Monday."""
    if dt.datetime.now().weekday() != 0:  # 0 = Monday
        return

    quote = random.choice(quotes)

    html_content = f"""
    <html>
        <body style="font-family: Arial, sans-serif; padding: 20px;">
            <h2 style="color: #2E86C1;">Monday Motivation</h2>
            <p style="font-size: 16px;">{quote}</p>
            <p style="font-size: 14px; color: gray;">Have a great week ahead!</p>
        </body>
    </html>
    """

    msg = EmailMessage()
    msg["Subject"] = "🌟 Monday Motivation 🌟"
    msg["From"] = MY_EMAIL
    msg["To"] = ", ".join(recipients)
    msg.set_content(quote)  # Fallback plain text
    msg.add_alternative(html_content, subtype="html")

    try:
        with smtplib.SMTP(SMTP_SERVER, 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")


# Run once and exit
send_monday_motivation()
