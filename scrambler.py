import pyperclip
import random
import keyboard
import tkinter
from tkinter import *

textString = "Text"
sLen = len(textString)
    
def scramble():
    newlist = ["nochar"]*sLen
    for char in textString:
        tryindex = random.randint(0,sLen-1)
        found = False
        while found is False:
            if newlist[tryindex] == "nochar":
                found = True
                newlist[tryindex] = char
            else:
                if tryindex == 0:
                    tryindex = sLen
                tryindex-=1
            
    output = ""
    for thing in newlist:
        output+=thing
    return output
    
#checks to see if box is ticked when shortcut is pressed
def shell():
    if engage.get() == 1:
        pyperclip.copy(scramble())

keyboard.add_hotkey('ctrl+v', shell)

gui = tkinter.Tk()
gui.geometry("250x80")
gui.title("disaster")
engage = IntVar()
check = Checkbutton(gui, text = "Engage scramble", variable = engage, onvalue = 1, offvalue = 0, height=5, width = 20,command=shell)
check.pack()
gui.mainloop()
