from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Carlos"
message["to"] = "carlos@especializati.com.br"
message["subject"] = "Welcome to the Python"
message.attach(MIMEText("<h1>Hello</h1>", "html"))

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as smtp:
    smtp.login("d119d015fa68db", "474fcadbf5e2dd")
    smtp.send_message(message)
    print("Email sended")