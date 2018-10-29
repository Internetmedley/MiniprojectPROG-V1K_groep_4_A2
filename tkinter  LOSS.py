import base64, PIL
from tkinter import *
from PIL import ImageTk
from urllib.request import urlopen
from io import BytesIO
import scoredisplay
import json

root = Tk()
score = 44


def username_clicked():
    global score
    with open('hi-scores.json', 'r') as f:
        jsontext = json.load(f)

    if len(usernameEntry.get()) > 14:
        usernameLabel["text"] = "That username is too long, please try again."
        return
    elif len(usernameEntry.get()) < 2:
        usernameLabel["text"] = "That username is too short, please try again."
        return
    elif usernameEntry.get() in jsontext.keys():                        # anders fuckt het met de dictionary en values
        usernameLabel["text"] = "That username is already being used, please try another one."
        return
    else:
        jsontext.update({usernameEntry.get(): score})
        submitUsername.destroy()

    lijstKeys = (sorted(jsontext, key=jsontext.__getitem__, reverse=True))              # maakt lijst van keys van reverse gesorteerde values
    lijstValues = (sorted(jsontext.values(), reverse=True))                         # maakt lijst van reverse gesorteerde values

    jsontext.clear()
    for i in range(0, 10):
        try:
            jsontext.update({lijstKeys[i]: lijstValues[i]})
        except KeyError:
            break

    with open('hi-scores.json', 'w') as f:
            json.dump(jsontext, f)
    return




usernameEntry = Entry(master=winnersPage)
submitUsername = Button(master=winnersPage, text='SUBMIT', command=username_clicked)
usernameLabel = Label(master=winnersPage, text="Give username between 3 and 14 characters.")

with open('hi-scores.json', 'r') as f:
    data = json.load(f)
    if score > min(data.values()):
        usernameEntry.pack()
        submitUsername.pack()
        usernameLabel.pack()

root.mainloop()