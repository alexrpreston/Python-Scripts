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
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail



regex = re.compile(r'<[^>]+>')
def remove_html(string):
    return regex.sub('', string)

def sendText():
    bookNotes_dir = "/home/alex/jobs/Obsidian/Main/Resources/Book Notes"
    finalText = ""

    booksNotes = os.listdir(bookNotes_dir)
    
    for j in range(0,2):
        for i in range(0,2):
            randomBookIndex = random.randrange(0,len(booksNotes))
            randomBook = booksNotes[randomBookIndex]
            with open(bookNotes_dir + "/" + randomBook, 'r') as f:
                text = f.read()
                bookText = markdown.markdown(text)


            html = bs4.BeautifulSoup(bookText, "html.parser")
            quotes = html.find_all("li")

            if len(quotes) == 0:
                continue
            
            q = quotes[random.randrange(0, len(quotes))]
            finalText += randomBook[:len(randomBook)-2] + " \n"
            finalText += "-" + q.text.strip() + "\n\n"
        print(finalText)

        message = Mail(
            from_email='alex@pageamplify.com',
            to_emails='alexrpreston@gmail.com',
            subject='Book Highlights',
            html_content=finalText)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
        
            
def pullFromRepo():
    repo_path = '/home/alex/jobs/Obsidian'
    g = git.Repo(repo_path)
    token = os.environ.get('GITHUB_TOKEN')
    g.remotes.origin.pull(auth=(token, ""))
    sendText()
    
pullFromRepo()