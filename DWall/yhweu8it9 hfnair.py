import tkinter as tk
from PIL import Image, ImageTk

# Creating a tkinter widget
window = tk.Tk()

# Add title
window.title("Background Manager")

frame = tk.Frame(window, bg='black')
frame2 = tk.Frame(window)
frame.pack(side=tk.LEFT, expand=True)
frame2.pack(side=tk.LEFT, expand=True)

#Frame 1 widgets
tk.Button(frame, text = "Previous Background").grid(row=1, column=1)

load = Image.open("jupiter.jpg")
widthz, heightz = load.size
while widthz >= 600:
    load = load.resize((int(widthz/2), int(heightz/2)), Image.ANTIALIAS)
    widthz, heightz = load.size
render = ImageTk.PhotoImage(load)
img = tk.Label(frame, image=render)
img.grid(row=3, column=1)

#Frame 2 widgets
tk.Button(frame2, text = "Select Background").grid(row=1, column=1)


# Start GUI and main loop
window.mainloop()

