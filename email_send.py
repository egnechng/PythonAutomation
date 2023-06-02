import smtplib
import ssl
from email.message import EmailMessage

subject = "Python Email"

body = "test email"
sender_email = "eugenechang2003@gmail.com"
receiver_email = "egnechng@gmail.com"
password = input("Enter password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""
message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())