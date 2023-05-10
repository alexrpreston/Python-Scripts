from email import message
import os
from datetime import date
import math
import random
import markdown
import bs4
import re
import requests
import git
import os
from twilio.rest import Client



regex = re.compile(r'<[^>]+>')
def remove_html(string):
    return regex.sub('', string)

def sendText():
    bookNotes_dir = "/home/alex/jobs/Obsidian/Main/Resources/Book Notes"

    booksNotes = os.listdir(bookNotes_dir)
    randomBookIndex = random.randrange(0,len(booksNotes))
    randomBook = booksNotes[randomBookIndex]
    finalText = ""

    for i in range(0,5):
        with open(bookNotes_dir + "/" + randomBook, 'r') as f:
            text = f.read()
            bookText = markdown.markdown(text)


        html = bs4.BeautifulSoup(bookText, "html.parser")
        quotes = html.find_all("li")

        if len(quotes) == 0:
            continue
        

        text = randomBook[:len(randomBook)-2] + " \n"
        q = quotes[random.randrange(0, len(quotes))]
        finalText += randomBook + "\n"
        finalText += "-" + q.text + "\n\n"
    print(finalText)

    phoneNum = os.environ.get('PHONE_NUMBER')
    # Find your Account SID and Auth Token in Account Info
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_number = os.environ['TWILIO_NUMBER']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
            body=finalText,
            from_=twilio_number,
            to=phoneNum
    )

    print(message.sid)
 
            
def pullFromRepo():
    my_repo = git.Repo('/home/alex/jobs/Obsidian')
    my_repo.remotes.origin.pull()
    sendText()
    
pullFromRepo()