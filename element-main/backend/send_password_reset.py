import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from dotenv.main import load_dotenv
import os


# n = len(sys.argv)

# def send_email(sender_email, sender_password, recipient_email, subject, message):
#     # Set up the SMTP server
#     smtp_server = 'smtp.office365.com'
#     smtp_port = 587

#     # Create the email message
#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = recipient_email
#     msg['Subject'] = subject
#     msg.attach(MIMEText(message, 'plain'))

#     try:
#         # Connect to the SMTP server
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()

#         # Login to your Outlook account
#         server.login(sender_email, sender_password)

#         # Send the email
#         server.send_message(msg)
#         print('Email sent successfully!')

#     except Exception as e:
#         print('An error occurred while sending the email:', str(e))

#     finally:
#         # Close the connection to the SMTP server
#         server.quit()

# Get user input
sender_email = "elementreset@outlook.com"
load_dotenv()
sender_password = os.environ['SENDER_PASSWORD']
recipient_email = sys.argv[1]
subject = sys.argv[2]
message = sys.argv[3]

# Send the email
# send_email(sender_email, sender_password, recipient_email, subject, message)

import http.client
import json

conn = http.client.HTTPSConnection("ruthvik-mail.azurewebsites.net")

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Content-Type": "application/json" 
}

payload = json.dumps({
  "email": recipient_email,
  "subject": subject,
  "text": "Hello, this is a test email!"
}
)

conn.request("POST", "/api/ruthvik/triggers/When_a_HTTP_request_is_received/invoke?api-version=2022-05-01&sp=%2Ftriggers%2FWhen_a_HTTP_request_is_received%2Frun&sv=1.0&sig=uTw84cM2Ef7WQdS6ugB-SyBH3NCoU1ao8Bz9LL8_dbw", payload, headersList)
response = conn.getresponse()
result = response.read()

print(result.decode("utf-8"))