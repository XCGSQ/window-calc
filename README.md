# Window Calculator

A simple window calculator using the Tkinter library in Python.

## Usage

To use the window calculator, provide the desired height, width, and title in the `create_window` function. The window will appear with the given dimensions and title.

```python
import tkinter as tk

def create_window(width, height, title):
    root = tk.Tk()
    root.title(title)
    root.geometry(f"{width}x{height}")
    root.mainloop()

create_window(300, 200, "My Tk Window")
