from tkinter import *
root = Tk()
root.geometry('500x500')


lostframe= Frame(master=root)
lostframe.pack(side=TOP)

labelframe5= Label(master=lostframe,
              text='GAME OVER \n',
              font='times 60 bold',
              fg= 'red',
              bg='black',
              width= 10000,
              height=7)
labelframe5.pack()

blackframe= Label(master=root,
            bg='black',
            width=135000000,
            height=100)
blackframe.pack()


button_back_mainscreen= Button(master=blackframe,
                               text= 'Play\n'
                                     'again',
                               font= 'times 25',
                               fg='black',
                               height= 15,
                               width= 14)
button_back_mainscreen.pack(side=RIGHT)


button_back_mainscreen= Button(master=blackframe,
                               text= 'Back',
                               font= 'times 25',
                               fg='black',
                               height= 15,
                               width= 14)
button_back_mainscreen.pack(side=LEFT)

rightblackframe= Frame(master=blackframe,
                       width=1100,
                       bg='black')
rightblackframe.pack()

leftblackframe= Frame(master=blackframe,
                      width=1100,
                      bg='black')
leftblackframe.pack()

root.mainloop()