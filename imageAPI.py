from tkinter import *
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import APIcall

APIcall.ID_test()


root = Tk()


plaatje_url = APIcall.hero_image_URL()
print(APIcall.hero_image_URL())
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
