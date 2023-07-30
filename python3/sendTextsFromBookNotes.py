import requests
from bs4 import BeautifulSoup
import random
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def getRandomBooks(numOfBooks):
    urlToBookNotes = "https://alexpreston.org/bookshelf/"

    response = requests.get(urlToBookNotes)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    a_tags = soup.find_all('a')
    filtered_a_tags = [tag for tag in a_tags if tag.get('href') != "/"]
    return random.sample(filtered_a_tags, numOfBooks)



def getRandomHighlights(randomBooks, numHighlightsPerBook):
    highlights = {}
    for book in randomBooks:
        print(book.get('href'))
        url = "https://alexpreston.org" + book.get('href')
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        li_tags = soup.find_all('li')
        try:
            sampledHighlights = random.sample(li_tags, numHighlightsPerBook)
            highlights[book.text] = [highlight.text.strip() for highlight in sampledHighlights]
        except: 
            print("Couldn't grab highlights for", book.text)
    return highlights


def sendHighlights(highlights):
    textBody = ""
    for book in highlights.keys():
        textBody += "<p><u><b>" + book + "</b></u></p>"
        for highlight in highlights[book]:
            textBody += "<ul><li>" + highlight + "</li></ul>"
    
    message = Mail(
        from_email='alex@pageamplify.com',
        to_emails='alexrpreston@gmail.com',
        subject='Book Notes',
        html_content=textBody
    )
    try:
        key = os.environ.get('SENDGRID_API_KEY')
        sg = SendGridAPIClient(key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


def getHighlights():
    randomBooks = getRandomBooks(5)
    randomHighLights = getRandomHighlights(randomBooks, 1)
    sendHighlights(randomHighLights)

getHighlights()