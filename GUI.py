#region Imports

import APIcall
import scoredisplay
import os
from tkinter import *
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import base64

#endregion

# region Globals
score = 25

# endregion

# region Buttons


def restartButton():
    """Restarts the whole game so everything gets ressted"""
    python = sys.executable
    os.execl(python, python, * sys.argv)


def hintButton1():
    """Prints the first hint on click"""
    global score
    textGuessAnswer.insert(END, APIcall.hero_description() + '\n--------------------------------------------------\n')
    hint1Button.destroy()
    score -= 3
    scoreLabel["text"] = "SCORE: {}".format(score)

def hintButton2():
    """Print the second hint on click"""
    global score
    textGuessAnswer.insert(END, APIcall.hero_letters() + '\n--------------------------------------------------\n')
    hint2Button.destroy()
    score -= 3
    scoreLabel["text"] = "SCORE: {}".format(score)

def hintButton3():
    """Print the third hint on click"""
    global score
    textGuessAnswer.insert(END, APIcall.eerste_letter() + '\n-------------------------------------------------\n')
    hint3Button.destroy()
    score -= 3
    scoreLabel["text"] = "SCORE: {}".format(score)

def hintButton4():
    """Print the forth hint on click"""
    global score
    textGuessAnswer.insert(END, APIcall.hero_comics() + '\n--------------------------------------------------\n')
    hint4Button.destroy()
    score -= 3
    scoreLabel["text"] = "SCORE: {}".format(score)

def guessButtonClicked():
    """On click Compare user input with the random superhero form APIcall"""
    global score
    if enterSuperHero.get().lower() == APIcall.hero_name().lower():
        textGuessAnswer.insert(END, "U heeft het goed geraden!")
        winnersWindow()
    else:
        textGuessAnswer.insert(END, "U heeft het fout geraden!")
        score -= 1
        scoreLabel["text"] = "SCORE: {}".format(score)

#endregion

#region Windows

def buildStartScreen():
    """Forget all the other window packs and pack the startscreen and its buttons"""
    howToPlayScreen.pack_forget()
    highScoreScreen.pack_forget()
    mainGame.pack_forget()
    aboutPage.pack_forget()
    winnersPage.pack_forget()
    startScreen.pack(fill=BOTH, expand=True)
    quitButton.pack(side=BOTTOM)
    playButton.pack(side=BOTTOM)

def highScores():
    """Forget all the other window packs and only pack the highscore screen"""
    aboutPage.pack_forget()
    howToPlayScreen.pack_forget()
    startScreen.pack_forget()
    mainGame.pack_forget()
    highScoreScreen.pack(fill=BOTH, expand=True)

def howToPlay():
    """Forget all the other window packs and only pack the how to play screen"""
    aboutPage.pack_forget()
    highScoreScreen.pack_forget()
    mainGame.pack_forget()
    startScreen.pack_forget()
    howToPlayScreen.pack(fill=BOTH, expand=True)

def mainGameWindow():
    """First do a API call, disable the menu and forget all the other window packs than pack the main game"""
    #APIcall.ID_test()
    emptyMenu = Menu(root)
    root.config(menu=emptyMenu)
    aboutPage.pack_forget()
    howToPlayScreen.pack_forget()
    highScoreScreen.pack_forget()
    startScreen.pack_forget()
    winnersPage.pack_forget()
    mainGame.pack(fill=BOTH, expand=True)

def aboutWindow():
    """Forget all the other window packs and only pack the about us screen"""
    howToPlayScreen.pack_forget()
    highScoreScreen.pack_forget()
    startScreen.pack_forget()
    mainGame.pack_forget()
    aboutPage.pack(fill=BOTH, expand=True)

def winnersWindow():
    """Show the menu bar again and forget all the other window packs and only pack the winners screen"""
    root.config(menu=menubar)
    howToPlayScreen.pack_forget()
    highScoreScreen.pack_forget()
    startScreen.pack_forget()
    mainGame.pack_forget()
    aboutPage.pack_forget()
    winnersPage.pack(fill=BOTH, expand=True)


#endregion

#region tkinter Root

root = Tk()
root.title("SuperHero The Game")
root.geometry("1920x1080")

#endregion

#region Windows and Attributes

#Build startscreen and attributes
startScreen = Frame(master=root, bg="black")
startScreen.pack(fill=BOTH, expand=True)
playButton = Button(master=startScreen, text="PLAY", command=mainGameWindow, height=2, width=40, cursor="hand2")
quitButton = Button(master=startScreen, text="QUIT", command=root.quit, height=2, width=40, cursor="hand2")
quitButton.pack(side=BOTTOM, pady=55)
playButton.pack(side=BOTTOM, pady=2)

#Build highscorescreen and attributes
highScoreScreen = Frame(master=root, bg="black")
highScoreScreen.pack(fill=BOTH, expand=True)
backButtonScore = Button(master=highScoreScreen, text='HOME', command=buildStartScreen)
backButtonScore.pack(side=BOTTOM, padx=20, pady=60)
hiScoreLabel = Label(master=highScoreScreen, bg="black", fg="white", text="HIGH SCORES: \n " +scoredisplay.high_score_print(), font='times ')
hiScoreLabel.place(relx=0.5, rely=0.5, anchor=CENTER)


#Build howtoplayscreen and attributes
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

#Build the main game window and build attributes
mainGame = Frame(master=root, bg="black")
mainGame.pack(fill=BOTH, expand=True)
enterSuperHero = Entry(master=mainGame)
enterSuperHero.place(relx=0.5, rely=0.5, anchor=W)
labelEntryInput = Label(master=mainGame, bg="black", fg="white", text="ENTER A SUPERHERO:")
labelEntryInput.place(relx=0.5, rely=0.5, anchor =E)
textGuessAnswer = Text(master=mainGame, fg="white", bg="black", width=50, height=6, wrap=WORD, yscrollcommand=set())
guessButton = Button(master=mainGame, text="GUESS", command=guessButtonClicked)
giveUpButton = Button(master=mainGame, text="GIVE UP", )
guessButton.pack()
textGuessAnswer.pack()
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

#Build the about page and its attributes
aboutPage = Frame(master=root, bg="black")
labelframe1 = Label(master=aboutPage,text='About us and the game: \n',font='times 16 bold',fg= 'white',bg='black',width= 10000,height=5)
labelframe1.pack(side=TOP)
labelframe1= Label(master=aboutPage,
                   text='Our opinions going into this project: \n'
                   '\n'
                   'This game was made by a copple of students, studying at the HU in Utrecht.\n'
                   'We are five boys around the ages of 20 hoping to become an experienced programmer\n'
                   '"Tobias S: I realy enjoyed making this game even thought sometimes the error messages got the better of me."\n'
                   '"Remy d B: When we started, I did not know if it would be fun but after working on it with my team I started to enjoy this project a lot more."\n'
                   '"Jesse B: Starting the project was quite a struggle because I fas far behind with my knowledge but I have caught up for and thanks to my team, so I wanted to thank them again."\n'
                   '"Ramon P: I had difficulty visualising the project but after all the hard work we put I had a lot of fun."\n'
                   '"Jelle-Jetze H: I had difficulty taking the lead as projectleader but after all backup I received from my team I got a lot more confident in my role."\n',
                   fg= 'white',bg='black',font='times 11',width= 100000,height=10)
labelframe1.pack(side=TOP)
labelframe1 = Label(master=aboutPage,
                   text='Reason for creating this game:\n'
                   '\n'
                   'This game was originally a school project. We could choose from many different assignments but this one just stood out as project.\n'
                   'But what started as school-project ended in a fun hobby project with some new friends.\n'
                   "We let our imagination go loose on this project and we realy did not try to hold back",
fg= 'white', bg='black', font='times 11', width= 1000000,height=7)
labelframe1.pack(side=LEFT)
frame= Frame(master=root, bg='black')
frame.pack()
downframe = Frame(master=root)
downframe.pack(side=BOTTOM)
backButtonAbout = Button(master=aboutPage, text="HOME", command=buildStartScreen)

#Build winners window and attributes
winnersPage = Frame(master=root, bg="black")
labelWinMessage = Label(master=winnersPage, text='CONGRATIOLATIONS \n''You Win!\n',font='times 16 bold', fg= 'Yellow', bg='black')
labelWinMessage.pack()
backButtonWin = Button(master=winnersPage, text='PLAY AGIAN', fg='black', command=restartButton, height=2, width=40, cursor="hand2")
backButtonWin.place(relx=0.6, rely=0.88)
backButtonWin = Button(master=winnersPage, text='QUIT', fg='black', command=root.quit, height=2, width=40, cursor="hand2")
backButtonWin.place(relx=0.2, rely=0.88)

# Add a Drop-down menu to the start screen
menubar = Menu(root)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="How to play", command=howToPlay)
helpmenu.add_command(label="About us", command=aboutWindow)
helpmenu.add_command(label="Highscores", command=highScores)
menubar.add_cascade(label="Menu", menu=helpmenu)
root.config(menu=menubar)

#Call to URL to set application icon
iconU = urlopen("https://cdn3.iconfinder.com/data/icons/movie-company/129/MARVEL.png")
raw_data_icon = iconU.read()

b64_data = base64.encodebytes((raw_data_icon))
image = PhotoImage(data=b64_data)

root.tk.call('wm', 'iconphoto', root._w, image)
buildStartScreen()

#endregion

# start the application
root.mainloop()

