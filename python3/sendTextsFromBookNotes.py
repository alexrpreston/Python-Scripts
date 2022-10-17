import os
from datetime import date
import math
import random
import markdown
import bs4
import re
import requests
import git


regex = re.compile(r'<[^>]+>')
def remove_html(string):
    return regex.sub('', string)

def sendText():
    bookNotes_dir = "/home/alex/Obsidian/Main/Resources/Book Notes"

    booksNotes = os.listdir(bookNotes_dir)
    randomBookIndex = random.randrange(0,len(booksNotes))
    randomBook = booksNotes[randomBookIndex]

    with open(bookNotes_dir + "/" + randomBook, 'r') as f:
        text = f.read()
        bookText = markdown.markdown(text)


    html = bs4.BeautifulSoup(bookText, "html.parser")
    quotes = html.find_all("li")

    len(quotes)

    text = randomBook[:len(randomBook)-2] + " \n"
    while len(text) < 160:
        if len(quotes) > 0:
            q = quotes[random.randrange(0, len(quotes))]
            text += "➖" + q.text + "\n"
        else:
            print("exiting")
            exit()

    phoneNum = os.environ.get('phoneNumber')
    textBeltAPIKey = os.environ.get('textBeltAPIKey')
    payload = {
            'phone': phoneNum, 
            'message': text, 
            'key':textBeltAPIKey
    }
    resp = requests.post('https://textbelt.com/text', payload)
    print(resp)
    print("finished")
            
def pullFromRepo():
    my_repo = git.Repo('/home/alex/Obsidian')
    my_repo.remotes.origin.pull()
    sendText()
pullFromRepo()