from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from pathlib import Path
import smtplib

message = MIMEMultipart()
message["from"] = "Carlos"
message["to"] = "carlos@especializati.com.br"
message["subject"] = "Welcome to the Python"
message.attach(MIMEText("<h1>Hello</h1>", "html"))
message.attach(MIMEApplication(Path("09-useful/03-sending-emails-with-attachment.py").read_bytes()))

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as smtp:
    smtp.login("d119d015fa68db", "474fcadbf5e2dd")
    smtp.send_message(message)
    print("Email sended")