from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

message = MIMEMultipart()
message["from"] = "Vance Wamley"
message["to"] = "Enter Email"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))
# message.attach(MIMEImage(Path("Enter image").read_bytes))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("Your Email Here", "Your Pass")
    smtp.send_message(message)
    print("Sent...")
