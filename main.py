import requests
import send_email

topic = 'tesla'
api_key = '1300b2bc92f6422587d9122f0e0a0c2f'
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&"
       f"apiKey={api_key}"
       "language=en")
# Make request
request = requests.get(url)

#Get dict with data
content = request.json()

message = ""
# Access articles dicts
for article in content['articles'][0:20]:
    message = (f"{message}\n"
               f"Topic: {article['title']}\n"
               f"Articles: {article['description']}\n"
               f"{article['url']}\n")
# Sending mail
message = "Subject: Today's news" + '\n' + message
print(message)
send_email.send_emails(message.encode('utf-8'))

