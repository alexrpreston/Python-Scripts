import email, smtplib, ssl
import glob
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Test"
body = "Test"
sender_email = "alexrpreston1@gmail.com"
kindle_email = ['alexrpreston@gmail.com', 'alexrpreston_18919f@kindle.com', 'alexrpreston_dcefd3@kindle.com']
password = "@Cheese1015!"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(kindle_email)
message["Subject"] = subject
message["Bcc"] = kindle_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "/Users/alexpreston/Downloads/Parkinsons Law by Cyril Northcote Parkinson (z-lib.org).epub.mobi"
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, kindle_email, text)