import pyperclip, re


kindleHighlights = pyperclip.paste() #Grabs the text copied from my clipboard
kindleHighlights = re.sub("Notes and highlights for\n", "", kindleHighlights) #Removes Header
kindleHighlights = re.sub("Highlight.+\n", " ", kindleHighlights) #Removes where I highlighted each note from.

#Punctuation Spacing Isussues
kindleHighlights = re.sub(" \.", ".", kindleHighlights.rstrip()) 
kindleHighlights = re.sub(" ,", ",", kindleHighlights)
kindleHighlights = re.sub("\( ", "(", kindleHighlights)
kindleHighlights = re.sub(" \)", ")", kindleHighlights)
kindleHighlights = re.sub(" :", ":", kindleHighlights)
kindleHighlights = re.sub(" ;", ";", kindleHighlights)
kindleHighlights = re.sub(" - ", "-", kindleHighlights)

print(kindleHighlights)

#Remove Highlight (yellow) - Page 12 · Location 29 and replace with nothing
#Turn all ' .' into '.' 
