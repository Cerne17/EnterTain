import os
from os import startfile
from tkinter import *

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
    output.delete(0.0, END) #clears the text box

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