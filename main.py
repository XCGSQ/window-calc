import tkinter as tk

title = "Window Calculator | By XCGSQ"

def create_window(width, height):
    root = tk.Tk()
    root.title(title)
    root.geometry(f"{width}x{height}")
    root.mainloop()

create_window(700, 440)
