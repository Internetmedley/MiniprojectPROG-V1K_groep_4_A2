from tkinter import *
root = Tk()
root.geometry('500x500')
#hier moet nog komen welke character het is uit de APIcall

topframe= Frame(master=root,
                bg= 'black',
                height=100,
                width=100)
topframe.pack()

losetext= Label(master=topframe,
               text='YOU LOSE',
               fg='red',
               bg='black',
               font= 'times 80 bold',
               padx= 1000,
               pady=100)
losetext.pack(side=TOP)

pointtext= Label(master=topframe,
                 text= 'The character was {}!'.format(character),           #vul hier de functie van de character in
                 fg='white',
                 bg='black',
                 font='times 40 bold',
                 pady=100)
pointtext.pack(side=BOTTOM)

bottomframe_black= Frame(master=root,
                   bg='black',
                   height=1000,
                   width=1000)
bottomframe_black.pack(side=BOTTOM)

play_again_button_lose= Button(master=bottomframe_black,
                               text='Play\n Again',
                               font='times 30 bold',
                               height=10,
                               width=10)
play_again_button_lose.pack(side=RIGHT)

black_frame_lose= Frame(master=bottomframe_black,
                        width=1300)
black_frame_lose.pack(side=BOTTOM)

home_screen_button_lose= Button(master=bottomframe_black,
                               text='Home\n Screen',
                               font='times 30 bold',
                               height=10,
                               width=10)
home_screen_button_lose.pack(side=LEFT)

root.mainloop()