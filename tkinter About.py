from tkinter import *
root = Tk()
root.geometry('500x500')




leftframe= Frame(master=root)
leftframe.pack()

labelframe1= Label(master=leftframe,
              text='About us and the game: \n',
              font='times 30 bold',
              fg= 'white',
              bg='black',
              width= 10000,
              height=5)
labelframe1.pack(side=TOP)

labelframe1= Label(master=leftframe,
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
              font='times 16',
              width= 100000,
              height=10)
labelframe1.pack(side=TOP)

labelframe1= Label(master=leftframe,
              text='Reason for creating this game:\n'
                   '\n'
                   'This game was originally a school project. We could choose from many different assignments but this one just stood out as project.\n'
                   'But what started as school-project ended in a fun hobby project with some new friends.\n'
                   "We let our imagination go loose on this project and we realy did not try to hold back",
              fg= 'white',
              bg='black',
              font='times 16',
              width= 1000000,
              height=7)
labelframe1.pack(side=LEFT)

frame= Frame(master=root,
             bg= 'black')
frame.pack()



downframe= Frame(master=root)
downframe.pack(side=BOTTOM)

# button_back_mainscreen= Button(master=downframe,
#                                text= 'Back',
#                                font= 'times 25',
#                                fg='black',
#                                height= 15,
#                                width= 14)
# button_back_mainscreen.pack(side=LEFT)


labelframe2= Label(master=downframe,
                   text= '\n'
                         'Thank you for playing our game!'
                         '\n',
                   fg='pink',
                   bg='black',
                   font='times 40 bold',
                   width= 40,
                   height=1000)
labelframe2.pack()


frame2= Frame(master=root,
              bg= 'black')
frame.pack()



root.mainloop()