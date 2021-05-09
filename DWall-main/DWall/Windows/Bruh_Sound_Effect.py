import tkinter as tk
from tkinter import *
from playsound import playsound

root = Tk() 
root.title('Bruh Sound Eftect')
root.geometry("500x400")

def play():
    playsound('Sounds/Bruh Sound Effect #2.mp3')

play_button = Button(root, text="BRUH", font=("Helvetica", 32), relief=GROOVE, command=play)

play_button.pack();
