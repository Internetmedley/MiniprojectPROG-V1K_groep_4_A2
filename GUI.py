from tkinter import *
import APIcall

score = 25
hintKeuzeDict = {'1' : APIcall.hero_description(),
                 '2' : APIcall.hero_letters(),
                 '3' : APIcall.eerste_letter(),
                 '4' : APIcall.hero_comics()}



def hintButton1():
    global score
    labelGuessAwnser["text"] = hintKeuzeDict["1"]
    hint1Button.destroy()
    score -= 3
    scoreLabel["text"] = "SCORE: {}".format(score)


def hintButton2():
    global score
    labelGuessAwnser["text"] = hintKeuzeDict["2"]
    hint2Button.destroy()
    score -= 3
    scoreLabel["text"] = "SCORE: {}".format(score)

def hintButton3():
    global score
    labelGuessAwnser["text"] = hintKeuzeDict["3"]
    hint3Button.destroy()
    score -= 3
    scoreLabel["text"] = "SCORE: {}".format(score)


def hintButton4():
    global score
    labelGuessAwnser["text"] = hintKeuzeDict["4"]
    hint4Button.destroy()
    score -= 3
    scoreLabel["text"] = "SCORE: {}".format(score)

def guessButtonClicked():
    global score
    if enterSuperHero.get().lower() == APIcall.hero_name().lower():
        labelGuessAwnser["text"] = "U heeft het goed geraden!"
    else:
        labelGuessAwnser["text"] = "U heeft het fout geraden!"
        score -= 1
        scoreLabel["text"] = "SCORE: {}".format(score)


def buildStartScreen():
    howToPlayScreen.pack_forget()
    highScoreScreen.pack_forget()
    mainGame.pack_forget()
    AboutPage.pack_forget()
    startScreen.pack(fill=BOTH, expand=True)
    quitButton.pack(side=BOTTOM)
    playButton.pack(side=BOTTOM)


def highScores():
    AboutPage.pack_forget()
    howToPlayScreen.pack_forget()
    startScreen.pack_forget()
    mainGame.pack_forget()
    highScoreScreen.pack(fill=BOTH, expand=True)


def howToPlay():
    AboutPage.pack_forget()
    highScoreScreen.pack_forget()
    mainGame.pack_forget()
    startScreen.pack_forget()
    howToPlayScreen.pack(fill=BOTH, expand=True)


def mainGameWindow():
    emptyMenu = Menu(root)
    root.config(menu=emptyMenu)
    AboutPage.pack_forget()
    howToPlayScreen.pack_forget()
    highScoreScreen.pack_forget()
    startScreen.pack_forget()
    mainGame.pack(fill=BOTH, expand=True)


def AboutWindow():
    howToPlayScreen.pack_forget()
    highScoreScreen.pack_forget()
    startScreen.pack_forget()
    mainGame.pack_forget()
    AboutPage.pack(fill=BOTH, expand=True)

root = Tk()
root.title("SuperHero The Game")
root.geometry("1920x1080")


#Build startscreen and atributes
startScreen = Frame(master=root, bg="black")
startScreen.pack(fill=BOTH, expand=True)
playButton = Button(master=startScreen, text="PLAY", command=lambda: [mainGameWindow(), APIcall.ID_test()], height=2, width=40, cursor="hand2")
quitButton = Button(master=startScreen, text="QUIT", command=root.quit, height=2, width=40, cursor="hand2")
quitButton.pack(side=BOTTOM, pady=55)
playButton.pack(side=BOTTOM, pady=2)

#Build highscorescreen and atributes
highScoreScreen = Frame(master=root, bg="black")
highScoreScreen.pack(fill=BOTH, expand=True)
backButtonScore = Button(master=highScoreScreen, text='HOME', command=buildStartScreen)
backButtonScore.pack(side=BOTTOM, padx=20, pady=60)


#Build howtoplayscreen and atributes
howToPlayScreen = Frame(master=root, bg="black")
howToPlayScreen.pack(fill=BOTH, expand=True)
backButtonHowTo = Button(master=howToPlayScreen, text='HOME', command=buildStartScreen)
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
backButtonHowTo.pack(padx=100, pady=20)

hintDisplayDict = {'1': "Press 1 description of the character.",
                   '2': "Press 2 for the number of characters in the name.",
                   '3': "de eerste letter van het te raden character.",
                   '4': "een aantal comics waar het te raden character in voorkomt."}

#Build the main game window and build atributes
mainGame = Frame(master=root, bg="black")
mainGame.pack(fill=BOTH, expand=True)
enterSuperHero = Entry(master=mainGame)
enterSuperHero.place(relx=0.5, rely=0.5)
labelEntryInput = Label(master=mainGame, bg="black", fg="white", text="ENTER A SUPERHERO:")
labelEntryInput.place(relx=0.28, rely=0.5)
labelHints = Label(master=mainGame, bg="black", fg="white", text="{}\n {}\n {}\n {}\n".format(hintDisplayDict["1"], hintDisplayDict["2"],                                                                      hintDisplayDict["3"], hintDisplayDict["4"]))
labelHints.pack(side=TOP, pady=10, padx=0)
labelGuessAwnser = Label(master=mainGame, text="", fg="white", bg="black")
guessButton = Button(master=mainGame, text="GUESS", command=guessButtonClicked)
giveUpButton = Button()
guessButton.pack()
labelGuessAwnser.pack()
scoreLabel = Label(master=mainGame, bg="black", fg="white", text="SCORE: 25")
scoreLabel.place(relx=1.0, rely=0.0, anchor=NE)
hint1Button = Button(master=mainGame, text="Give description", command=hintButton1)
hint2Button = Button(master=mainGame, text="Give amount letters", command=hintButton2)
hint3Button = Button(master=mainGame, text="Give first letter of name", command=hintButton3)
hint4Button = Button(master=mainGame, text="Give comics in which the character appears", command=hintButton4)
hint1Button.place(relx=0.45, rely=0.3)
hint2Button.place(relx=0.53, rely=0.3)
hint3Button.place(relx=0.63, rely=0.3)
hint4Button.place(relx=0.26, rely=0.3)


#Build the about page and its atributes
AboutPage = Frame(master=root, bg="black")
labelframe1 = Label(master=AboutPage,
              text='About us and the game: \n',
              font='times 16 bold',
              fg= 'white',
              bg='black',
              width= 10000,
              height=5)
labelframe1.pack(side=TOP)

labelframe1= Label(master=AboutPage,
              text='Our opinions going into this project: \n'
                   '\n'
                   'This game was made by a copple of students, studying at the HU in Utrecht.\n'
                   'We are five boys around the ages of 20 hoping to become an experienced programmer\n'
                   '"Tobias S: I realy enjoyed making this game even thought sometimes the error messages got the better of me."\n'
                   '"Remy d B: When we started, I did not know if it would be fun but after working on it with my team I started to enjoy this project a lot more."\n'
                   '"Jesse B: Starting the project was quite a struggle because I fas far behind with my knowledge but I have caught up for and thanks to my team, so I wanted to thank them again."\n'
                   '"Ramon P: I had difficulty visualising the project but after all the hard work we put I had a lot of fun."\n'
                   '"Jelle-Jetze H: I had difficulty taking the lead as projectleader but after all backup I received from my team I got a lot more confident in my role."\n',
              fg= 'white',
              bg='black',
              font='times 11',
              width= 100000,
              height=10)
labelframe1.pack(side=TOP)

labelframe1= Label(master=AboutPage,
              text='Reason for creating this game:\n'
                   '\n'
                   'This game was originally a school project. We could choose from many different assignments but this one just stood out as project.\n'
                   'But what started as school-project ended in a fun hobby project with some new friends.\n'
                   "We let our imagination go loose on this project and we realy did not try to hold back",
              fg= 'white',
              bg='black',
              font='times 11',
              width= 1000000,
              height=7)
labelframe1.pack(side=LEFT)

frame= Frame(master=root, bg='black')
frame.pack()

downframe= Frame(master=root)
downframe.pack(side=BOTTOM)
backButtonAbout = Button(master=AboutPage, text="HOME", command=buildStartScreen)

root.iconbitmap("C:/Users/ramon/Downloads/marvel.ico")
buildStartScreen()

# Add a Drop-down menu to the startscreen
menubar = Menu(root)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="How to play", command=howToPlay)
helpmenu.add_command(label="About us", command=AboutWindow)
helpmenu.add_command(label="Highscores", command=highScores)
menubar.add_cascade(label="Menu", menu=helpmenu)
root.config(menu=menubar)

# start the application
root.mainloop()

