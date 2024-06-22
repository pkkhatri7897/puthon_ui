import datetime
import os
import time
import pandas as pd
import numpy as np
import threading

import tkinter as tk
# from tkinter import messagebox, filedialog, Toplevel, Label, Entry, Button
# import tkinter.font as tkFont
import ttkbootstrap as ttk
from screeninfo import get_monitors
import ctypes
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame


import serial
import struct


class Reader():
    def __init__(self, root):
        self.root = root
        self.style = ttk.Style()
        combobox_font = ("Helvetica", 8)  # Adjust the font family and size as needed
        # self.style.configure('TCombobox', font=combobox_font, background="orange")
        # self.style.configure('TLabelframe.Label', font=combobox_font, background='orange')  # Set the background color

        
        
        
        ###############################################################################        
        # THEME SELECTION
        ###############################################################################    
        # THEME ROOT    
        self.theme_root = ttk.Frame(self.root)
        self.theme_label_frame = tk.ttk.LabelFrame(self.theme_root, text="Themes", height=5, width=80, bootstyle="secondary")
        self.theme_label_frame.pack()
        self.theme_var = tk.StringVar()
        self.theme_var.set("minty")
        self.theme_combobox = ttk.Combobox(self.theme_label_frame, textvariable=self.theme_var, values=self.get_theme_list(self.style), height=3, width=15)
        # self.theme_combobox.configure(style="TCombobox")
        self.theme_combobox.pack(pady=5, padx=5)
        self.theme_combobox.bind("<<ComboboxSelected>>", self.apply_theme)
        self.theme_root.place(relx=0.80, rely=0.02)
        ###############################################################################        


        ###############################################################################        
        # OPERATIONS 
        ############################################################################### 
        
        # BUTTON FONT STYLE
        self.opr_btn_font = ttk.Style()
        self.opr_btn_style_type = "info.Link.TButton"
        self.opr_btn_font.configure(self.opr_btn_style_type, font=(14))

        # OPERATION ROOT
        self.operation_root = ttk.Frame(self.root)
        self.operation_label = tk.ttk.LabelFrame(self.operation_root, text="Operations", bootstyle="secondary", height=60, width=500)
        self.operation_label.pack_propagate(False)
        self.operation_label.pack(padx=5, pady=5, fill='both', expand=True)
        
        # BUTTONS
        self.clear_all = ttk.Button(self.operation_label, text="Clear_all", command=self.clear_all, bootstyle="success-link", style=self.opr_btn_style_type)
        self.clear_all.grid(row=0, column=0, padx=40, pady=5)
        
        self.clear_all = ttk.Button(self.operation_label, text="Actions", command=self.actions, bootstyle="success-link", style=self.opr_btn_style_type)
        self.clear_all.grid(row=0, column=1, padx=40, pady=5)

        self.clear_all = ttk.Button(self.operation_label, text="Tags", command=self.tags, bootstyle="success-link", style=self.opr_btn_style_type)
        self.clear_all.grid(row=0, column=2, padx=40, pady=5)

        self.operation_root.place(relx=0.15, rely=0.15)
        ###############################################################################        

    
    def get_theme_list(self, ttk_style):
        # Get the list of available themes from the ttkbootstrap module
        return ttk_style.theme_names()
    

    def apply_custom_styles(self):
        self.opr_btn_font = ttk.Style()
        self.opr_btn_style_type = "info.Link.TButton"
        self.opr_btn_font.configure(self.opr_btn_style_type, font=(14))


    def apply_theme(self, event):
        # Apply the selected theme
        selected_theme = self.theme_var.get()
        self.style.theme_use(selected_theme)
        self.apply_custom_styles()
        print(f"Theme '{selected_theme}' applied successfully!")


    def clear_all(self):
        pass


    def actions(self):
        pass


    def tags(self):
        pass


if __name__=="__main__":
    screen_resolution = [(m.width, m.height) for m in get_monitors()]
    # root = ttk.Window(title="orange@Accent-systems", size=screen_resolution[0])
    root = ttk.Window(title="orange@Accent-systems", size=(800, 480))
    app = Reader(root)
    root.mainloop()