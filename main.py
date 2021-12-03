import os
from os import startfile
from os import system
from tkinter import *

# Programs list:
programDict = {"yt": "www.youtube.com", "discord": "C:\\Users\\MIGUEL\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe", "twitter": "www.twitter.com", "lol": "\"D:\\Riot Games\\Riot Client\\RiotClientServices.exe\" --launch-product=league_of_legends --launch-patchline=live", "vscode": "\"C:\\Users\\MIGUEL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe\"", "chrome": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", "wpp": "\"C:\\Users\\MIGUEL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe\"", "spotify": "C:\\Users\\MIGUEL\\AppData\\Roaming\\Spotify\\Spotify.exe"}

# Color Variables:
mainText = "#DC143C"
secondaryText = "#FAFAFA"
comentaryText = "#CD5C5C"

mainBg = "#1C1C1C"
secondaryBg = "#191919"
thirdBg = "#000"
fourthBg= "#FAFAFA"


# Function of the click event
def click():
    enteredPrograms = textentry.get() #gets the text box value
    textentry.delete(0, END) #clears the text box
    listOfInputs = enteredPrograms.split()
    for element in listOfInputs:
        try:
            startfile(str(detection(element)))
        except:
            system(str(detection(element)))

# Function that detects wether the program is or not in the program list:
def detection(inputedData):
    return programDict[str(inputedData)]

# Function to open apps


# Create a Canvas
window = Tk()
window.title("EnterTain")
window.configure(width=1200, height=800, bg=mainBg)
canvas = Canvas(window)

# Text
Label (window, text="\nType bellow the Programs you want to open (yt,vscode,lol,steam,discord,chrome):\n", bg=mainBg, fg=mainText, font="none 24 bold") .grid (row=1, column=0)

# Input
textentry = Entry (window, width=70, bg=fourthBg ,fg=mainText, font="none 14 bold")
textentry.grid (row=2,column=0)

# Submit Button

Label (window, text="If you are sure, press Submit \n\n", font ="none 18 underline", bg=mainBg, fg=comentaryText) .grid(row=3, column=0)

Button (window, text="\nSubmit\n", width=15, height=1, bg=mainText, fg=mainBg, font="none 18 bold", command=click) .grid(row=4, column=0, sticky=S)

# sets what is supposed to keep runing in the Canvas
window.mainloop()