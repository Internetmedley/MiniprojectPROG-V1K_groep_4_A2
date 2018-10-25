from tkinter import *
from tkinter.messagebox import showinfo
from PROG import APIcall

# def mouseOverHandelEvent(self,Event):
#     bericht="deze shit werkt"
#     showinfo(title="popup", message=bericht)

score = 25

def guessButtonClicked():
    global score
    if enterSuperHero.get().lower() == APIcall.hero_name().lower():
        guessButtonAnswer["text"] = "U heeft het goed geraden!"
    else:
        guessButtonAnswer["text"] = "U heeft het fout geraden!"
        score -= 1
        scoreLabel["text"] = "SCORE: {}".format(score)


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
playButton = Button(master=startScreen, text="PLAY", command=lambda:[mainGameWindow(), APIcall.ID_test()], height=2, width=40, cursor="hand2")
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
text.insert(INSERT,  "When you start to play the game you get 25 points. \n"
                    "You have 2 choices: You can either buy a hint or you can guess the character. \n"
                    "The goal of the game is that you guess the marvel Character with the help of tips that you can buy. \n"
                    "If you buy a hint, you loose 3 points. \n"
                    "There are 4 different hints you can choose from. \n"
                    "Tip 1 : You get a small description about the character. \n"
                    "tip 2 : You get the 1st letter of the name of the character. \n"
                    "tip 3 : You get to see the marvel comics the character has played in. \n"
                    "tip 4 : You get to see how many characters there are in the name of the character. \n"
                    "If you guess the character wrong, you loose 1 point. \n")
text.pack()
backButtonHowTo.pack(side=BOTTOM, pady=20)

hintDisplayDict = {'1': "Press 1 description of the character.",
                   '2': "Press 2 for the number of characters in the name.",
                   '3': "de eerste letter van het te raden character.",
                   '4': "een aantal comics waar het te raden character in voorkomt."}

mainGame = Frame(master=root, bg="black")
mainGame.pack(fill=BOTH, expand=True)
enterSuperHero = Entry(master=mainGame)
enterSuperHero.place(relx=0.5, rely=0.5, anchor=W)
labelEntryInput = Label(master=mainGame, bg="black", fg="white", text="ENTER A SUPERHERO:")
labelEntryInput.place(relx=0.5, rely=0.5, anchor=E)
labelHints = Label(master=mainGame, bg="black", fg="white", text="{}\n {}\n {}\n {}\n".format(hintDisplayDict["1"], hintDisplayDict["2"], hintDisplayDict["3"], hintDisplayDict["4"]))
scoreLabel = Label(master=mainGame, bg="black", fg="white", text = "SCORE: 25")
guessButton = Button(master=mainGame, text="GUESS", command=guessButtonClicked)
guessButtonAnswer = Label(master=mainGame, text='', bg="black", fg="white")
scoreLabel.place(relx=1.0, rely=0.0, anchor=NE)
labelHints.pack(side=TOP, pady=10, padx=0)
guessButton.pack()
guessButtonAnswer.pack()


# root.iconbitmap("C:/Users/ramon/Downloads/marvel.ico")
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

