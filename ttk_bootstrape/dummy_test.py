

###### change labelframe bg color

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def change_bg_color():
    style.configure('Custom.TLabelframe', background='#ADD8E6')  # Light Blue color
    label_frame.configure(style='Custom.TLabelframe')

root = ttk.Window(themename="flatly")

# Create a style object
style = ttk.Style()

# Create a LabelFrame
label_frame = ttk.LabelFrame(root, text="My Label Frame", width=200, height=100)
label_frame.pack(pady=20, padx=20)

# Create a Button to change the background color
change_color_button = ttk.Button(root, text="Change Background Color", command=change_bg_color)
change_color_button.pack(pady=10)

root.mainloop()
