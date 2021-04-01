import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from wallpaper import get_wallpaper, set_wallpaper
import ctypes

def change_wall(): 
    
    try: 
        set_wallpaper(str(path.get()))
        check = "success"
  
    except: 

        print(path.get())
        check = "Wallpaper not found !"
    result.set(check) 
  
  
def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"))) 
    path.set(filename) 
      
    label_file_explorer.configure(text="File Opened: "+filename)
    image()
    return filename

window = tk.Tk() 
window.configure(bg='light grey') 

result = StringVar() 
path = StringVar() 

window.title("Background Manager")
  
b = Button(window, text="Open", command=browseFiles, bg="white") 
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)
  
c = Button(window, text="Apply", command=change_wall, bg="white") 
c.grid(row=2, column=2, columnspan=2, rowspan=2, padx=5, pady=5,) 

def image():
   load = Image.open(path.get())
   widthz, heightz = load.size
   while widthz >= 600:
       load = load.resize((int(widthz/2), int(heightz/2)), Image.ANTIALIAS)
       widthz, heightz = load.size
   render = ImageTk.PhotoImage(load)
   img = tk.Label(window, image=render)
   img.grid(row=5, column=1)

window.mainloop()



