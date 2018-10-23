from tkinter import *
from tkinter.messagebox import showinfo


# def mouseOverHandelEvent(self,Event):
#     bericht="deze shit werkt"
#     showinfo(title="popup", message=bericht)


def buildStartScreen():
    howToPlayScreen.pack_forget()
    highScoreScreen.pack_forget()
    mainGame.pack_forget()
    startScreen.pack(fill=BOTH, expand=True)
    quitButton.pack(side=BOTTOM)
    playButton.pack(side=BOTTOM)


def highScores():
    howToPlayScreen.pack_forget()
    startScreen.pack_forget()
    mainGame.pack_forget()
    highScoreScreen.pack(fill=BOTH, expand=True)


def howToPlay():
    highScoreScreen.pack_forget()
    mainGame.pack_forget()
    startScreen.pack_forget()
    howToPlayScreen.pack(fill=BOTH, expand=True)

def mainGameWindow():
    howToPlayScreen.pack_forget()
    highScoreScreen.pack_forget()
    startScreen.pack_forget()
    mainGame.pack(fill=BOTH, expand=True)

root = Tk()
root.title("SuperHero The Game")
root.geometry("600x600")


#Build startscreen and atributes
startScreen = Frame(master=root, bg="black")
startScreen.pack(fill=BOTH, expand=True)
playButton = Button(master=startScreen, text="PLAY", command=mainGameWindow, height=2, width=40, cursor="hand2")
quitButton = Button(master=startScreen, text="QUIT", command=root.quit, height=2, width=40, cursor="hand2")
quitButton.pack(side=BOTTOM, pady=10)
playButton.pack(side=BOTTOM, pady=20)

#Build highscorescreen and atributes
highScoreScreen = Frame(master=root, bg="black")
highScoreScreen.pack(fill=BOTH, expand=True)
backButtonScore = Button(master=highScoreScreen, text='Back', command=buildStartScreen)
backButtonScore.pack(side=BOTTOM, pady=20)

#Build howtoplayscreen and atributes
howToPlayScreen = Frame(master=root, bg="black")
howToPlayScreen.pack(fill=BOTH, expand=True)
backButtonHowTo = Button(master=howToPlayScreen, text='Back', command=buildStartScreen)
text = Text(howToPlayScreen, bg="black", fg="white")
text.insert(INSERT, "Waneer je het spell start krijg je 25 punten. \n"
                    "Je hebt 2 keuzes: je kan een hint kopen en je kan een guess doen. \n"
                    "Je moet raden welke marvel character het is met behulp van hints te kopen. \n"
                    "Wanneer je een hint koopt verlies je 3 punten. \n"
                    "Er zijn 5 verschillende hints: \n"
                    "1 description, geeft een zin over de character. \n"
                    "2 je krijgt de eerste letters te zien van de naam. \n"
                    "3 je krijgt te zien in welke marvel commics de character heeft gezeten. \n"
                    "4 je krijgt te zien hoevel letters in de naam zit. \n"
                    "5 je krijgt een plaatje te zien van de character. \n"
                    "Bij een verkeerde Guess verlies je 1 punt \n")
text.pack()
backButtonHowTo.pack(side=BOTTOM, pady=20)

hintDisplayDict = {'1': "Press 1 description of the character.",
                   '2': "Press 2 for the number of characters in the name.",
                   '3': "de eerste letter van het te raden character.",
                   '4': "een aantal comics waar het te raden character in voorkomt."}

mainGame = Frame(master=root, bg="black")
mainGame.pack(fill=BOTH, expand=True)
enterSuperHero = Entry(master=mainGame)
enterSuperHero.place(relx=0.5, rely=0.5)
labelEntryInput = Label(master=mainGame, bg="black", fg="white", text="ENTER A SUPERHERO:")
labelEntryInput.place(relx=0.3, rely=0.5)
labelHints = Label(master=mainGame, bg="black", fg="white", text="{}\n {}\n {}\n {}\n".format(hintDisplayDict["1"], hintDisplayDict["2"],
                                                                      hintDisplayDict["3"], hintDisplayDict["4"]))
labelHints.pack(side=TOP, pady=10, padx=0)

root.iconbitmap("C:/Users/ramon/Downloads/marvel.ico")
buildStartScreen()

# Drop down menu op begin scherm
menubar = Menu(root)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="How to play", command=howToPlay)
helpmenu.add_command(label="About us")
helpmenu.add_command(label="Highscores", command=highScores)
menubar.add_cascade(label="Menu", menu=helpmenu)

root.config(menu=menubar)

root.mainloop()

