from pygame import mixer # Load the required library
import time
import threading

def music():
    mixer.init()
    mixer.music.load('C:\\Users\\remyd\\Downloads\\Avengers Suite (Theme).mp3')
    mixer.music.play()


def DoPrint():
        print("Hello")

start_music = threading.Thread(target=music())
start_print = threading.Thread(target=DoPrint())
start_print.start()

