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
    mixer.music.load("Avengers_Suite_Theme.mp3")
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
                giveUsernameLabel["text"] = "That username is too long, please try again."
                return
            elif len(usernameEntry.get()) < 3:
                giveUsernameLabel["text"] = "That username is too short, please try again."
                return
            elif usernameEntry.get() in allTimeDict.keys() or usernameEntry.get() in dailyDict[vandaag]:                        # anders werkt het niet met de dictionary en values
                giveUsernameLabel["text"] = "That username is already being used, please try another one."
                return
            else:
                submitUsername.destroy()
                dictInDailyDictWithoutDate.update({usernameEntry.get(): score})

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
            if len(usernameEntry.get()) > 14:
                giveUsernameLabel["text"] = "That username is too long, please try again."
                return
            elif len(usernameEntry.get()) < 3:
                giveUsernameLabel["text"] = "That username is too short, please try again."
                return
            elif usernameEntry.get() in allTimeDict.keys(): # anders werkt het niet met de dictionary en values
                giveUsernameLabel["text"] = "That username is already being used, please try another one."
                return
            else:
                submitUsername.destroy()
                with open('daily-hi-score.json', 'w') as f:
                    json.dump({vandaag: {usernameEntry.get(): score, "PLAYER 1": 0, "PLAYER 2": 0, "PLAYER 3": 0, "PLAYER 4": 0}}, f)

        allTimeDict.update({usernameEntry.get(): score})


        if score > min(allTimeDict.values()):
            lijstKeysAllTimeHighScore = (sorted(allTimeDict, key=allTimeDict.__getitem__, reverse=True))       # maakt lijst van keys van reverse gesorteerde values
            lijstValuesAllTimeHighScore = (sorted(allTimeDict.values(), reverse=True))                         # maakt lijst van reverse gesorteerde values

            allTimeDict.clear()
            for i in range(0, 10):
                try:
                    allTimeDict.update({lijstKeysAllTimeHighScore[i]: lijstValuesAllTimeHighScore[i]})
                except IndexError:
                    break

            with open('hi-scores.json', 'w') as f:
                    json.dump(allTimeDict, f)
        return

    def commentRemove():
        commentLabel["text"] = ""

    def restartButton():
        """Restarts the whole game so everything gets ressted"""
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def hintButton1():
        """Prints the first hint on click"""
        global score, numberOfHintsLeft
        if score <= 4:
            commentLabel["text"] = "You don't have enough points to ask for a hint!"
            root.after(1000, commentRemove)
            return
        textGuessAnswer.configure(state='normal')
        textGuessAnswer.insert(END, APIcall.hero_description() + '\n\n\t     -< scroll to go down >-\n\n')
        textGuessAnswer.configure(state='disabled')
        hint1Button.destroy()
        score -= 3
        numberOfHintsLeft -= 1
        hintLabel["text"] = "HINTS: {}".format(numberOfHintsLeft)
        scoreLabel["text"] = "SCORE: {}".format(score)

    def hintButton2():
        """Print the second hint on click"""
        global score, numberOfHintsLeft
        if score <= 4:
            commentLabel["text"] = "You don't have enough points to ask for a hint!"
            root.after(1000, commentRemove)
            return
        textGuessAnswer.configure(state='normal')
        textGuessAnswer.insert(END, APIcall.hero_letters() + '\n\n\t     -< scroll to go down >-\n\n')
        textGuessAnswer.configure(state='disabled')
        hint2Button.destroy()
        score -= 3
        numberOfHintsLeft -= 1
        hintLabel["text"] = "HINTS: {}".format(numberOfHintsLeft)
        scoreLabel["text"] = "SCORE: {}".format(score)

    def hintButton3():
        """Print the third hint on click"""
        global score, numberOfHintsLeft
        if score <= 4:
            commentLabel["text"] = "You don't have enough points to ask for a hint!"
            root.after(1000, commentRemove)
            return
        textGuessAnswer.configure(state='normal')
        textGuessAnswer.insert(END, APIcall.eerste_letter() + '\n\n\t     -< scroll to go down >-\n\n')
        textGuessAnswer.configure(state='disabled')
        hint3Button.destroy()
        score -= 3
        numberOfHintsLeft -= 1
        hintLabel["text"] = "HINTS: {}".format(numberOfHintsLeft)
        scoreLabel["text"] = "SCORE: {}".format(score)

    def hintButton4():
        """Print the forth hint on click"""
        global score, numberOfHintsLeft
        if score <= 4:
            commentLabel["text"] = "You don't have enough points to ask for a hint!"
            root.after(1000, commentRemove)
            return
        textGuessAnswer.configure(state='normal')
        textGuessAnswer.insert(END, APIcall.hero_comics() + '\n\n\t     -< scroll to go down >-\n\n')
        textGuessAnswer.configure(state='disabled')
        hint4Button.destroy()
        score -= 3
        numberOfHintsLeft -= 1
        hintLabel["text"] = "HINTS: {}".format(numberOfHintsLeft)
        scoreLabel["text"] = "SCORE: {}".format(score)

    def guessButtonClicked():
        """On click Compare user input with the random superhero form APIcall"""
        global score
        if enterSuperHero.get().lower() == APIcall.hero_name().lower():
            commentLabel["text"] = "You gave the right awnser!"
            giveUpButton.configure(command=lambda: None)
            giveUpButton.configure(cursor='')
            root.after(667, winnersWindow)
        else:
            score -= 1
            scoreLabel["text"] = "SCORE: {}".format(score)
            if score >= 0:
                commentLabel["text"] = "Oh no, you gave the wrong awnser!"
            if score == 0:
                commentLabel["text"] = "Oh no, you could not guess the character!"
                guessButton.configure(command=lambda: None)
                guessButton.configure(cursor='')
                root.after(667, lossWindow)
            root.after(1000, commentRemove)



    #endregion

    #region Windows

    def buildStartScreen():
        """Forget all the other window packs and pack the startscreen and its buttons"""
        howToPlayScreen.pack_forget()
        highScoreScreen.pack_forget()
        mainGame.pack_forget()
        aboutPage.pack_forget()
        winnersPage.pack_forget()

        start_screen_image_url = "https://images-na.ssl-images-amazon.com/images/I/91YWN2-mI6L._SL1500_.jpg"
        u = urlopen(start_screen_image_url)
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        size = 1145, 754
        im.thumbnail(size)
        photo = ImageTk.PhotoImage(im)
        homeImageLabel = Label(master=startScreen, image=photo)
        homeImageLabel.image = photo
        homeImageLabel.place(relx=0.4, rely=0.01, anchor=N)
        startScreen.pack(fill=BOTH, expand=True)

    def highScores():
        """Forget all the other window packs and only pack the highscore screen"""
        aboutPage.pack_forget()
        howToPlayScreen.pack_forget()
        startScreen.pack_forget()
        mainGame.pack_forget()
        winnersPage.pack_forget()
        hiScoreLabel["text"] = "ALL-TIME HIGHSCORES: \n\n" + scoredisplay.high_score_print()
        dailyHiScoreLabel["text"] = "DAILY HIGHSCORES {}: \n\n".format(date.strftime(date.today(), "%d-%m-%Y")) + scoredisplay.daily_high_scores_print()
        highScoreScreen.pack(fill=BOTH, expand=True)

    def howToPlay():
        """Forget all the other window packs and only pack the how to play screen"""
        aboutPage.pack_forget()
        howToPlayScreen.pack_forget()
        startScreen.pack_forget()
        mainGame.pack_forget()
        winnersPage.pack_forget()
        highScoreScreen.pack_forget()
        howToPlayScreen.pack(fill=BOTH, expand=True)

    def loading():
        """Sets information.json using APIcall.ID_test en updates loading text"""
        numbers = threading.Thread(target=APIcall.ID_test, daemon=True)
        numbers.start()
        pressPlayToStartLabel.place(relx=0.84, anchor=W)

        while numbers.is_alive():
            pressPlayToStartLabel["text"] = "Loading"
            root.after(333, root.update())
            while pressPlayToStartLabel["text"] != "Loading...":
                pressPlayToStartLabel["text"] += "."
                root.after(333, root.update())
        return

    def mainGameWindow():
        """First do loading(), then disable the menu and forget all the other window packs than pack the main game"""
        loading()
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
        winnersPage.pack_forget()
        aboutPage.pack(fill=BOTH, expand=True)

    def winnersWindow():
        """Show the menu bar again and forget all the other window packs and only pack the winners screen"""
        howToPlayScreen.pack_forget()
        highScoreScreen.pack_forget()
        startScreen.pack_forget()
        mainGame.pack_forget()
        aboutPage.pack_forget()
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
            if score > min(dataAllTimeHighScores.values()) or score > min(dataDailyHighScores[str(date.today())].values()):
                usernameLabel["text"] = "The character was {}!".format(APIcall.hero_name())
                usernameLabel.pack()
                giveUsernameLabel.pack()
                usernameEntry.pack(padx=20, pady=10)
                submitUsername.pack()
            else:
                usernameLabel["text"] = "The character was {}!".format(APIcall.hero_name())
                giveUsernameLabel["text"] = "You score is not high enough to enter the high-scores."
                usernameLabel.pack()
                giveUsernameLabel.pack()
        except KeyError:
            pass
        winnersPage.pack(fill=BOTH, expand=True)

    def lossWindow():
        howToPlayScreen.pack_forget()
        highScoreScreen.pack_forget()
        startScreen.pack_forget()
        mainGame.pack_forget()
        aboutPage.pack_forget()
        labelWinMessage.pack_forget()
        image_url = APIcall.hero_image_URL()
        u = urlopen(image_url)
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        photo = ImageTk.PhotoImage(im)
        heroImage = Label(master=lossPage, image=photo)
        heroImage.image = photo
        heroImage.pack()
        pointtext['text'] = 'The character was {}!'.format(APIcall.hero_name())
        pointtext.pack()
        lossPage.pack(fill=BOTH, expand=True)

    #endregion

    #region tkinter Root

    root = Tk()
    root.title("M.A.R.V.")
    root.geometry('480x480')
    root.state('zoomed')


    #endregion

    # region Windows and Attributes

    # Build start screen and attributes
    startScreen = Frame(master=root, bg="black")
    startScreen.pack(fill=BOTH, expand=True)
    playButton = Button(master=startScreen, text="PLAY", command=mainGameWindow, width=20, cursor="hand2", font='Fixedsys 18')
    quitButton = Button(master=startScreen, text="QUIT", command=root.quit, width=20, cursor="hand2", font='Fixedsys 18')
    playButton.place(relx=0.995, rely=0.01, anchor=NE)
    quitButton.place(relx=0.995, rely=0.085, anchor=NE)
    startScreenLabel = Label(master=startScreen, text="Welcome to\nM.A.R.V.!", bg="black", fg="white", font='Fixedsys 18')
    startScreenLabel.place(relx=0.945, rely=0.35, anchor=NE)
    pressPlayToStartLabel = Label(master=startScreen, text="Press PLAY to start!", bg="black", fg="white", font='Fixedsys 18')
    pressPlayToStartLabel.place(relx=0.89, rely=0.5, anchor=CENTER)


    # Build high score screen and attributes
    highScoreScreen = Frame(master=root, bg="black")
    highScoreScreen.pack(fill=BOTH, expand=True)
    backButtonScore = Button(master=highScoreScreen, text='HOME', command=buildStartScreen, font='Fixedsys 14 bold', width=8, cursor="hand2")
    backButtonScore.place(relx=0.5, rely=0.95, anchor=S)
    hiScoreLabel = Label(master=highScoreScreen, bg="black", fg="white", text='', font='Fixedsys 18')
    hiScoreLabel.place(relx=0.25, rely=0.2, anchor=N)
    dailyHiScoreLabel = Label(master=highScoreScreen, bg="black", fg="white", text='', font='Fixedsys 18')
    dailyHiScoreLabel.place(relx=0.75, rely=0.2, anchor=N)

    # Build the how to play screen and attributes
    howToPlayScreen = Frame(master=root, bg="black")
    howToPlayScreen.pack(fill=BOTH, expand=True)
    backButtonHowTo = Button(master=howToPlayScreen, text='HOME', command=buildStartScreen, font='Fixedsys 14 bold', width=8, cursor="hand2")
    howToPlayText = Text(howToPlayScreen, bg="black", fg="white", font='Fixedsys', wrap=WORD)
    howToPlayText.insert(INSERT,  "When you start to play the game you get 25 points. \n"
                        "You have 2 choices: You can either buy a hint or you can guess the character. \n"
                        "The goal of the game is that you guess the marvel Character with the help of tips that you can buy. \n"
                        "If you buy a hint, you loose 3 points. \n"
                        "There are 4 different hints you can choose from. \n"
                        "Tip 1 : You get a small description about the character. \n"
                        "tip 2 : You get the 1st letter of the name of the character. \n"
                        "tip 3 : You get to see the marvel comics the character has played in. \n"
                        "tip 4 : You get to see how many characters there are in the name of the character. \n"
                        "If you guess the character wrong, you loose 1 point. \n")
    howToPlayText.configure(state='disabled')
    howToPlayText.place(relx=0.5, rely=0.35, anchor=CENTER)
    backButtonHowTo.place(relx=0.5, rely=0.95, anchor=S)

    # Build the main game window and build attributes
    mainGame = Frame(master=root, bg="black")
    mainGame.pack(fill=BOTH, expand=True)
    enterSuperHero = Entry(master=mainGame, font='Fixedsys 18')
    enterSuperHero.place(relx=0.5, rely=0.5, anchor=CENTER)
    labelEntryInput = Label(master=mainGame, bg="black", fg="white", text="ENTER A CHARACTER:", font='Fixedsys 18')
    labelEntryInput.place(relx=0.285, rely=0.5, anchor=CENTER)
    textGuessAnswer = Text(master=mainGame, fg="white", bg="black", width=50, height=16, wrap=WORD, yscrollcommand=set(), font='Fixedsys 12')
    guessButton = Button(master=mainGame, text="GUESS", command=guessButtonClicked, font='Fixedsys 14 bold', width=10, cursor="hand2")
    guessButton.place(relx=0.715, rely=0.5, anchor=CENTER)
    giveUpButton = Button(master=mainGame, text="I GIVE UP", font='Fixedsys 14 bold', command=lossWindow, width=10, cursor="hand2")
    giveUpButton.place(relx=0.5, rely=0.8, anchor=CENTER)
    textGuessAnswer.place(relx=0.5, rely=0.080, anchor=N)
    scoreLabel = Label(master=mainGame, bg="black", fg="white", text="SCORE: 25", font='Fixedsys 18')
    scoreLabel.place(relx=0.995, rely=0.005, anchor=NE)
    hintLabel = Label(master=mainGame, bg="black", fg="white", text="HINTS: {}".format(numberOfHintsLeft), font='Fixedsys 18')
    hintLabel.place(relx=0.18, rely=0.005, anchor=N)
    displayLabel = Label(master=mainGame, bg="black", fg="white", text="DISPLAY:", font='Fixedsys 18')
    displayLabel.place(relx=0.5, rely=0.005, anchor=N)
    commentLabel = Label(master=mainGame, bg="black", fg="white", text="", font='Fixedsys')
    commentLabel.place(relx=0.5, rely=0.45, anchor=CENTER)
    hint1Button = Button(master=mainGame, text="Give DESCRIPTION!", command=hintButton1, font='Fixedsys 12', width=45, cursor="hand2")
    hint2Button = Button(master=mainGame, text="Give amount LETTERS!", command=hintButton2, font='Fixedsys 12', width=45, cursor="hand2")
    hint3Button = Button(master=mainGame, text="Give FIRST LETTER of NAME!", command=hintButton3, font='Fixedsys 12', width=45, cursor="hand2")
    hint4Button = Button(master=mainGame, text="Give COMICS of CHARACTER appearance!", command=hintButton4, font='Fixedsys 12', width=45, cursor="hand2")
    hint1Button.place(relx=0.18, rely=0.080, anchor=N)
    hint2Button.place(relx=0.18, rely=0.125, anchor=N)
    hint3Button.place(relx=0.18, rely=0.170, anchor=N)
    hint4Button.place(relx=0.18, rely=0.215, anchor=N)


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
    fg= 'white', bg='black', font='Fixedsys', width=1000000, height=7)
    labelframe1.pack(side=LEFT)
    frame= Frame(master=root, bg='black')
    frame.pack()
    downframe = Frame(master=root)
    downframe.pack(side=BOTTOM)
    backButtonAbout = Button(master=aboutPage, text='HOME', command=buildStartScreen, font='Fixedsys 14 bold', width=8, cursor="hand2")
    backButtonAbout.place(relx=0.5, rely=0.95, anchor=S)

    # Build winners window and attributes
    winnersPage = Frame(master=root, bg="black")
    labelWinMessage = Label(master=winnersPage, text='CONGRATULATIONS!\nYOU WIN', font='Fixedsys 18', fg='Lime', bg='black')
    backButtonWin = Button(master=winnersPage, text='RETURN TO HOME', fg='black', command=restartButton, height=1, width=20, cursor="hand2", font='Fixedsys 14 bold')
    backButtonWin.place(relx=0.5, rely=0.9, anchor=CENTER)
    usernameEntry = Entry(master=winnersPage, font='Fixedsys')
    submitUsername = Button(master=winnersPage, text='SUBMIT', command=username_submit_for_all_time_highscore, font='Fixedsys', width=8, cursor="hand2")
    usernameLabel = Label(master=winnersPage, bg="black", fg="yellow", text="", font='Fixedsys 18')
    giveUsernameLabel = Label(master=winnersPage, bg="black", fg="white", text="Give username between 3 and 14 characters below and press submit to enter the high-scores!", font='Fixedsys')
    # Build the loss window and attributes
    lossPage = Frame(master=root, bg="black")
    losetext = Label(master=lossPage, text='GAME OVER!\nYOU LOSE', fg='red', bg='black', font='Fixedsys 18')
    losetext.pack(side=TOP)
    pointtext = Label(master=lossPage,
    text='The character was {}!'.format(APIcall.hero_name()),  # vul hier de functie van de character in
    fg='yellow',bg='black',font='Fixedsys 18')
    black_frame_lose = Frame(master=lossPage)
    black_frame_lose.pack(side=BOTTOM)
    home_screen_button_lose = Button(master=lossPage,text='RETURN TO HOME', font='Fixedsys 14 bold', command=restartButton, cursor="hand2", height=1, width=20)
    home_screen_button_lose.place(relx=0.5, rely=0.9, anchor=CENTER)

    copyRightLabel = Label(master=root, bg="black", fg="white", font='Fixedsys 14', text='©Taakstrafmannen 2018')
    copyRightLabel.place(relx=0.995, rely=0.99, anchor=SE)

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
start_music = threading.Thread(target=music)
# Starts the music process thread
start_music.start()

# Builds a process thread to run the game in
start_print = threading.Thread(target=Game)
# Starts the game process thread
start_print.start()
# endregion
