from tkinter import  *
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
from PROG import APIcall



informatie = APIcall.ID_test()
plaatje_url = informatie['data']['results'][0]['thumbnail']['path'] + '.' + informatie['data']['results'][0]['thumbnail']['extension']
print(plaatje_url)

#plaatje_url = 'http://i.annihil.us/u/prod/marvel/i/mg/8/20/4c002f4a15c1c.jpg'



root = Tk()

u = urlopen(plaatje_url)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
photo = ImageTk.PhotoImage(im)

label = Label(master=root, image=photo)
label.image = photo
label.pack(fill=BOTH, expand=True)

button = Button(master=label, text='Druk hier')
button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()