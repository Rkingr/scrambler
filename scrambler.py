import pyperclip
import random
import keyboard
import tkinter
from tkinter import *

text = list("Text")           #put text in "", will split into a list for easy randomization

def scramble():
    global text
    output=""
    while len(text) > 0:
        output+=text.pop(random.randint(0,len(text)-1))
    text = list(output)
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
