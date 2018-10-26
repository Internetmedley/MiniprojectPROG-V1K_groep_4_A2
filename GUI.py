#region Imports
import APIcall
import scoredisplay
import os
from tkinter import *
from PIL import Image, ImageTk
from urllib.request import urlopen
import base64
import json
from io import BytesIO
from pygame import mixer
import threading
from datetime import date
#endregion

# region Globals
# The score of the player on start of the game
score = 25
numberOfHintsLeft = 4

# endregion

# region Game


def music():
    """Call mixer and play marvel theme as background music"""
    mixer.init()
    mixer.music.load("C:\\Users\\remyd\\Downloads\\Avengers_Suite_Theme.mp3")
    mixer.music.play(-1)


def Game():
    """Build the al the windows and attributes"""

    # region Buttons

    def username_submit_for_all_time_highscore():
        global score
        vandaag = str(date.today())
        with open('hi-scores.json', 'r') as f:
            allTimeDict = json.load(f)
        with open('daily-hi-score.json', 'r') as f:
            dailyDict = json.load(f)
        try:
            dictInDailyDictWithoutDate = dailyDict[vandaag]
            if len(usernameEntry.get()) > 14:
                usernameLabel["text"] = "That username is too long, please try again."
                return
            elif len(usernameEntry.get()) < 3:
                usernameLabel["text"] = "That username is too short, please try again."
                return
            elif usernameEntry.get() in allTimeDict.keys() or usernameEntry.get() in dailyDict[vandaag]:                        # anders werkt het niet met de dictionary en values
                usernameLabel["text"] = "That username is already being used, please try another one."
                return
            else:
                dictInDailyDictWithoutDate.update({usernameEntry.get(): score})
                allTimeDict.update({usernameEntry.get(): score})
                submitUsername.destroy()

                if score > min(dictInDailyDictWithoutDate.values()):
                    lijstKeysDailyHighScore = (sorted(dictInDailyDictWithoutDate, key=dictInDailyDictWithoutDate.__getitem__,reverse=True))  # maakt lijst van keys van reverse gesorteerde values
                    lijstValuesDailyHighScore = (sorted(dictInDailyDictWithoutDate.values(), reverse=True))  # maakt lijst van reverse gesorteerde values

                    dictInDailyDictWithoutDate.clear()
                    for i in range(0, 5):
                        try:
                            dictInDailyDictWithoutDate.update({lijstKeysDailyHighScore[i]: lijstValuesDailyHighScore[i]})
                        except IndexError:
                            break
                    with open('daily-hi-score.json', 'w') as f:
                        json.dump({vandaag: dictInDailyDictWithoutDate}, f)
        except KeyError:
            with open('daily-hi-score.json', 'w') as f:
                json.dump({vandaag: {usernameEntry.get(): score}}, f)

        if score > min(allTimeDict.values()):
            lijstKeysAllTimeHighScore = (sorted(allTimeDict, key=allTimeDict.__getitem__, reverse=True))              # maakt lijst van keys van reverse gesorteerde values
            lijstValuesAllTimeHighScore = (sorted(allTimeDict.values(), reverse=True))                         # maakt lijst van reverse gesorteerde values

            allTimeDict.clear()
            for i in range(0, 10):
                try:
                    allTimeDict.update({lijstKeysAllTimeHighScore[i]: lijstValuesAllTimeHighScore[i]})
                except KeyError:
                    break

            with open('hi-scores.json', 'w') as f:
                    json.dump(allTimeDict, f)
        return

    def restartButton():
        """Restarts the whole game so everything gets ressted"""
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def hintButton1():
        """Prints the first hint on click"""
        global score, numberOfHintsLeft
        textGuessAnswer.insert(END, APIcall.hero_description() + '\n\n\t      -< scroll to go down >-\n\n')
        hint1Button.destroy()
        score -= 3
        numberOfHintsLeft -= 1
        hintLabel["text"] = "HINTS: {}".format(numberOfHintsLeft)
        scoreLabel["text"] = "SCORE: {}".format(score)

    def hintButton2():
        """Print the second hint on click"""
        global score, numberOfHintsLeft
        textGuessAnswer.insert(END, APIcall.hero_letters() + '\n\n\t      -< scroll to go down >-\n\n')
        hint2Button.destroy()
        score -= 3
        numberOfHintsLeft -= 1
        hintLabel["text"] = "HINTS: {}".format(numberOfHintsLeft)
        scoreLabel["text"] = "SCORE: {}".format(score)

    def hintButton3():
        """Print the third hint on click"""
        global score, numberOfHintsLeft
        textGuessAnswer.insert(END, APIcall.eerste_letter() + '\n\n\t      -< scroll to go down >-\n\n')
        hint3Button.destroy()
        score -= 3
        numberOfHintsLeft -= 1
        hintLabel["text"] = "HINTS: {}".format(numberOfHintsLeft)
        scoreLabel["text"] = "SCORE: {}".format(score)

    def hintButton4():
        """Print the forth hint on click"""
        global score, numberOfHintsLeft
        textGuessAnswer.insert(END, APIcall.hero_comics() + '\n\n\t      -< scroll to go down >-\n\n')
        hint4Button.destroy()
        score -= 3
        numberOfHintsLeft -= 1
        hintLabel["text"] = "HINTS: {}".format(numberOfHintsLeft)
        scoreLabel["text"] = "SCORE: {}".format(score)

    def guessButtonClicked():
        """On click Compare user input with the random superhero form APIcall"""
        global score
        if enterSuperHero.get().lower() == APIcall.hero_name().lower():
            textGuessAnswer.insert(END, "You gave the right awnser!")
            winnersWindow()
        else:
            textGuessAnswer.insert(END, "Oeps you gave the wrong awnser!")
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
        hiScoreLabel["text"] = "ALL-TIME HIGHSCORES: \n\n" + scoredisplay.high_score_print()
        dailyHiScoreLabel["text"] = "DAILY HIGHSCORES {}: \n\n".format(str(date.today())) + scoredisplay.daily_high_scores_print()
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
        # APIcall.ID_test()
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
        labelWinMessage.pack()
        image_url = APIcall.hero_image_URL()
        u = urlopen(image_url)
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        photo = ImageTk.PhotoImage(im)
        heroImageLabel = Label(master=winnersPage, image=photo)
        heroImageLabel.image = photo
        heroImageLabel.pack()
        with open('hi-scores.json', 'r') as f:
            dataAllTimeHighScores = json.load(f)
        with open('daily-hi-score.json', 'r') as f:
            dataDailyHighScores = json.load(f)
        try:
            if score > min(dataAllTimeHighScores.values()) or score > min(dataDailyHighScores[str(date.today())]):
                usernameLabel["text"] = "The character was: {}!\n" \
                                        "Give username between 3 and 14 characters.".format(APIcall.hero_name())
                usernameLabel.pack()
                usernameEntry.pack()
                submitUsername.pack()
            else:
                usernameLabel["text"] = "The character was: {}!\n" \
                                        "Your score is not high enough to be in the high-score!".format(APIcall.hero_name())
                usernameLabel.pack()
        except KeyError:
            pass


    #endregion

    #region tkinter Root

    root = Tk()
    root.title("SuperHero The Game")
    root.state('zoomed')


    #endregion

    # region Windows and Attributes

    # Build start screen and attributes
    startScreen = Frame(master=root, bg="black")
    startScreen.pack(fill=BOTH, expand=True)
    playButton = Button(master=startScreen, text="PLAY", command=mainGameWindow, height=2, width=40, cursor="hand2", font='Fixedsys')
    quitButton = Button(master=startScreen, text="QUIT", command=root.quit, height=2, width=40, cursor="hand2", font='Fixedsys')
    quitButton.pack(side=BOTTOM, pady=55)
    playButton.pack(side=BOTTOM, pady=2)

    # Build high score screen and attributes
    highScoreScreen = Frame(master=root, bg="black")
    highScoreScreen.pack(fill=BOTH, expand=True)
    backButtonScore = Button(master=highScoreScreen, text='HOME', command=buildStartScreen, font='Fixedsys')
    backButtonScore.pack(side=BOTTOM, padx=20, pady=60)
    hiScoreLabel = Label(master=highScoreScreen, bg="black", fg="white", text='', font='Fixedsys 18')
    hiScoreLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Build the how to play screen and attributes
    hiScoreLabel.place(relx=0.25, rely=0.2, anchor=N)
    dailyHiScoreLabel = Label(master=highScoreScreen, bg="black", fg="white", text='', font='Fixedsys 18')
    dailyHiScoreLabel.place(relx=0.75, rely=0.2, anchor=N)

    #Build howtoplayscreen and attributes
    howToPlayScreen = Frame(master=root, bg="black")
    howToPlayScreen.pack(fill=BOTH, expand=True)
    backButtonHowTo = Button(master=howToPlayScreen, text='HOME', command=buildStartScreen, font='Fixedsys')
    text = Text(howToPlayScreen, bg="black", fg="white", font='Fixedsys')
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

    # Build the main game window and build attributes
    mainGame = Frame(master=root, bg="black")
    mainGame.pack(fill=BOTH, expand=True)
    enterSuperHero = Entry(master=mainGame, font='Fixedsys 18')
    enterSuperHero.place(relx=0.505, rely=0.5, anchor=W)
    labelEntryInput = Label(master=mainGame, bg="black", fg="white", text="ENTER A CHARACTER:", font='Fixedsys 18')
    labelEntryInput.place(relx=0.495, rely=0.5, anchor =E)
    textGuessAnswer = Text(master=mainGame, fg="white", bg="black", width=50, height=6, wrap=WORD, yscrollcommand=set(), font='Fixedsys')
    guessButton = Button(master=mainGame, text="GUESS", command=guessButtonClicked, font='Fixedsys')
    giveUpButton = Button(master=mainGame, text="I GIVE UP", font='Fixedsys')
    guessButton.pack()
    giveUpButton.pack()
    textGuessAnswer.pack()
    scoreLabel = Label(master=mainGame, bg="black", fg="white", text="SCORE: 25", font='Fixedsys 18')
    scoreLabel.place(relx=0.995, rely=0.005, anchor=NE)
    hintLabel = Label(master=mainGame, bg="black", fg="white", text="HINTS: {}".format(numberOfHintsLeft), font='Fixedsys 18')
    hintLabel.place(relx=0.18, rely=0.005, anchor=N)
    hint1Button = Button(master=mainGame, text="Give DESCRIPTION!", command=hintButton1, font='Fixedsys 12', width=45, cursor="hand2")
    hint2Button = Button(master=mainGame, text="Give amount LETTERS!", command=hintButton2, font='Fixedsys 12', width=45, cursor="hand2")
    hint3Button = Button(master=mainGame, text="Give FIRST LETTER of NAME!", command=hintButton3, font='Fixedsys 12', width=45, cursor="hand2")
    hint4Button = Button(master=mainGame, text="Give COMICS of CHARACTER appearance!", command=hintButton4, font='Fixedsys 12', width=45, cursor="hand2")
    hint1Button.place(relx=0.18, rely=0.080, anchor=CENTER)
    hint2Button.place(relx=0.18, rely=0.125, anchor=CENTER)
    hint3Button.place(relx=0.18, rely=0.170, anchor=CENTER)
    hint4Button.place(relx=0.18, rely=0.215, anchor=CENTER)


    # Build the about page and its attributes
    aboutPage = Frame(master=root, bg="black")
    labelframe1 = Label(master=aboutPage,text='About us and the game: \n', font='Fixedsys',fg= 'white', bg='black', width= 10000, height=5)
    labelframe1.pack(side=TOP)
    labelframe1 = Label(master=aboutPage,
                       text='Our opinions going into this project: \n'
                       '\n'
                       'This game was made by a copple of students, studying at the HU in Utrecht.\n'
                       'We are five boys around the ages of 20 hoping to become an experienced programmer\n'
                       '"Tobias S: I realy enjoyed making this game even thought sometimes the error messages got the better of me."\n'
                       '"Remy d B: When we started, I did not know if it would be fun but after working on it with my team I started to enjoy this project a lot more."\n'
                       '"Jesse B: Starting the project was quite a struggle because I fas far behind with my knowledge but I have caught up for and thanks to my team, so I wanted to thank them again."\n'
                       '"Ramon P: I had difficulty visualising the project but after all the hard work we put I had a lot of fun."\n'
                       '"Jelle-Jetze H: I had difficulty taking the lead as projectleader but after all backup I received from my team I got a lot more confident in my role."\n',
                       fg= 'white',bg='black', font='Fixedsys',width= 100000,height=10)
    labelframe1.pack(side=TOP)
    labelframe1 = Label(master=aboutPage,
                       text='Reason for creating this game:\n'
                       '\n'
                       'This game was originally a school project. We could choose from many different assignments but this one just stood out as project.\n'
                       'But what started as school-project ended in a fun hobby project with some new friends.\n'
                       "We let our imagination go loose on this project and we realy did not try to hold back",
    fg= 'white', bg='black', font='Fixedsys', width= 1000000,height=7)
    labelframe1.pack(side=LEFT)
    frame= Frame(master=root, bg='black')
    frame.pack()
    downframe = Frame(master=root)
    downframe.pack(side=BOTTOM)
    backButtonAbout = Button(master=aboutPage, text="HOME", command=buildStartScreen, font='Fixedsys')
    backButtonAbout.pack()

    # Build winners window and attributes
    winnersPage = Frame(master=root, bg="black")
    labelWinMessage = Label(master=winnersPage, text='CONGRATIOLATIONS \n''You Win!\n', font='Fixedsys', fg= 'Yellow', bg='black')
    backButtonWin = Button(master=winnersPage, text='PLAY AGIAN', fg='black', command=restartButton, height=2, width=40, cursor="hand2", font='Fixedsys')
    backButtonWin.place(relx=0.6, rely=0.88)
    backButtonWin = Button(master=winnersPage, text='QUIT', fg='black', command=root.quit, height=2, width=40, cursor="hand2", font='Fixedsys')
    backButtonWin.place(relx=0.2, rely=0.88)
    usernameEntry = Entry(master=winnersPage, font='Fixedsys')
    submitUsername = Button(master=winnersPage, text='SUBMIT', command=username_submit_for_all_time_highscore, font='Fixedsys')
    usernameLabel = Label(master=winnersPage, bg="black", fg="white", text="", font='Fixedsys')

    # Add a Drop-down menu to the start screen
    menubar = Menu(root)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="How to play", command=howToPlay, font='Fixedsys')
    helpmenu.add_command(label="About us", command=aboutWindow, font='Fixedsys')
    helpmenu.add_command(label="Highscores", command=highScores, font='Fixedsys')
    menubar.add_cascade(label="Menu", menu=helpmenu, font='Fixedsys')
    root.config(menu=menubar)

    # Call to URL to set application icon
    iconU = urlopen("https://cdn3.iconfinder.com/data/icons/movie-company/129/MARVEL.png")
    raw_data_icon = iconU.read()
    b64_data = base64.encodebytes((raw_data_icon))
    image = PhotoImage(data=b64_data)
    root.tk.call('wm', 'iconphoto', root._w, image)
    buildStartScreen()

    # endregion

    # start the application
    root.mainloop()
# endregion

# region Multi-threading
# NOTE on threads: We use threads so the game and game music can run as separate processes on the CPU


# Builds a process thread to run the game music in
start_music = threading.Thread(target=music())
# Starts the music process thread
start_music.start()

# Builds a process thread to run the game in
start_print = threading.Thread(target=Game())
# Starts the game process thread
start_print.start()
# endregion
