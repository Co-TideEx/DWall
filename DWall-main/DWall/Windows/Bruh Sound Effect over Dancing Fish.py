import tkinter as tk
from tkinter import *
from playsound import playsound
from PIL import Image, ImageTk

root = Tk() 
root.title('Bruh Sound Eftect')
root.geometry("500x400")

def play():
    while 1==1:
        sleep()
        playsound('Sounds/Bruh Sound Effect #2.mp3')

def image():
    load = Image.open('Windows\Images.gif')
    widthz, heightz = load.size
    
    while widthz >= 600:
        load = load.resize((int(widthz/2), int(heightz/2)), Image.ANTIALIAS)
        widthz, heightz = load.size

    canv = tk.Canvas(window, height=str(heightz), width=str(widthz))
    canv.grid(row=3, column=1)
    
    render = ImageTk.PhotoImage(load)
    canv.create_image(str((widthz/2)), str(heightz/2), image = render)

play_button.pack();


root.mainLoop()
