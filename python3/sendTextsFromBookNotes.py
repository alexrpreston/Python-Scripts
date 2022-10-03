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
            exit()

    payload = {
            'phone': '3217492467', 
            'message': text, 
            'key':'4478955e074ccfba8225c1b10ccc3d4fb13eb1832SFOC2LRLmalDac3bSF6yCmzv'
    }
    resp = requests.post('https://textbelt.com/text', payload)

    print("finished")
            
def pullFromRepo():
    my_repo = git.Repo('/home/alex/Obsidian')
    my_repo.remotes.origin.pull()
    sendText()
pullFromRepo()