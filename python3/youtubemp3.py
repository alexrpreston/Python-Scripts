from pytube import YouTube
import os, pyperclip, time
youtubeLink = pyperclip.paste() #Grabs the text copied from my clipboard
print(youtubeLink)
yt = YouTube(youtubeLink)
stream = yt.streams.filter(only_audio=True).first()
videoTitle = yt.title
stream.download('/Users/alexpreston/Downloads/'+yt.title) 
print("Finished downloading.")
