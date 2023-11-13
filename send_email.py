import smtplib
import ssl
import os


def send_emails(message):
    host = "smtp.gmail.com"
    port = 465

    password = os.getenv("PASSWORD_news_api")
    username = "gadiner1@gmail.com"

    receiver = "gadiner1@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)