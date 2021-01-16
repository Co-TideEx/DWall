import tkinter as tk

# Creating a tkinter widget
window = tk.Tk()

# Add title
window.title("Background Manager")

frame = tk.Frame(window)
frame2 = tk.Frame(window)
frame.pack(side=tk.LEFT)

tk.Button(frame, text = "Previous Background").pack()
#tk.setImage()

tk.Button(frame2, text = "Select Background").pack()
#tk.setImage()


# Start GUI and main loop
window.mainloop()

