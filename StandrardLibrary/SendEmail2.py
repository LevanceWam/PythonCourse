from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("Templates.html").read_text())

message = MIMEMultipart()
message["from"] = "Vance Wamley"
message["to"] = "Enter Email"
message["subject"] = "This is a test"
body = template.substitute(name="John")
message.attach(MIMEText(body,  "html"))
# message.attach(MIMEImage(Path("Enter image").read_bytes))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("Your Email Here", "Your Pass")
    smtp.send_message(message)
    print("Sent...")
