from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import smtplib
from string import Template

template = Template(Path("09-useful/04-template.html").read_text())
body = template.substitute({ "name": "Carlos" })

message = MIMEMultipart()
message["from"] = "Carlos"
message["to"] = "carlos@especializati.com.br"
message["subject"] = "Welcome to the Python"
# message.attach(MIMEText("<h1>Hello</h1>", "html"))
message.attach(MIMEText(body, "html"))

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as smtp:
    smtp.login("d119d015fa68db", "474fcadbf5e2dd")
    smtp.send_message(message)
    print("Email sended")