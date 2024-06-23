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
import tkinter.font as tkFont
from PIL import Image, ImageTk


import serial
import struct


class Reader():
    def __init__(self, root):
        self.root = root
        self.style = ttk.Style()
        combobox_font = ("Helvetica", 8)  # Adjust the font family and size as needed
        # self.style.configure('TCombobox', font=combobox_font, background="orange")
        # self.style.configure('TLabelframe.Label', font=combobox_font, background='orange')  # Set the background color
        
        # Apply the default theme
        self.default_theme = "vapor"
        self.style.theme_use(self.default_theme)


        ###############################################################################        
        # CSV PATH & VARIABLE OF ACTIONS
        ###############################################################################    
        # VARIABLE
        self.action_name = "Entrance"
        self.time_duration = 5

        # CSV
        self.tags_details = []
        self.tags_references = {}
        # self.home_loc = os.path.expanduser('')
        self.home_loc = os.getcwd()
        self.orange_rfid = os.path.join(self.home_loc, "orange")
        os.makedirs(self.orange_rfid, exist_ok=True)
        self.tags_details_csv = os.path.join(self.orange_rfid, "tags_details.csv")

        ###############################################################################  


        ###############################################################################        
        # LOGO
        ###############################################################################

        # Create a frame to hold the image
        self.image_frame = ttk.Frame(self.root)
        self.image_frame.pack(padx=20, pady=20)

        # Load and resize the image
        image_path = "orange\orange.png"  # Replace with your image path
        original_image = Image.open(image_path)
        resized_image = original_image.resize((200, 50), Image.LANCZOS)  # Adjust size as needed
        self.image = ImageTk.PhotoImage(resized_image)

        # Create a label to display the image
        self.image_label = ttk.Label(self.image_frame, image=self.image)
        self.image_label.pack()

        self.image_frame.place(relx=0.02, rely=0.02)
        ###############################################################################  
        
        
        ###############################################################################        
        # THEME SELECTION
        ###############################################################################    
        # THEME ROOT    
        self.theme_root = ttk.Frame(self.root)
        self.theme_label_frame = tk.ttk.LabelFrame(self.theme_root, text="Themes", height=5, width=80, bootstyle="secondary")
        self.theme_label_frame.pack()
        self.theme_var = tk.StringVar()
        self.theme_var.set("vapor")
        self.theme_combobox = ttk.Combobox(self.theme_label_frame, textvariable=self.theme_var, values=self.get_theme_list(self.style), height=3, width=15, state="readonly")
        self.theme_combobox.pack(pady=5, padx=5)
        self.theme_combobox.bind("<<ComboboxSelected>>", self.apply_theme)
        self.theme_root.place(relx=0.80, rely=0.02)
        ###############################################################################        


        ###############################################################################        
        # OPERATIONS 
        ############################################################################### 
        
        # # BUTTON FONT STYLE
        # self.opr_btn_font = ttk.Style()
        # self.opr_btn_style_type = "info.Link.TButton"
        # self.opr_btn_font.configure(self.opr_btn_style_type, font=(14))

        # # POPUP BUTTON FONT STYLE
        # self.pop_btn_font = ttk.Style()
        # self.pop_btn_style_type = "success.Link.TButton"
        # self.pop_btn_font.configure(self.opr_btn_style_type, font=(11))

        self.apply_custom_styles()

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


        ###############################################################################        
        # MAIN FRAME TREEVIEW
        ###############################################################################
        # CREATE ROOT OF MAINFRAME EXCEL
        self.main_entry_root = ttk.Frame(self.root)
        self.main_entry_label = tk.ttk.LabelFrame(self.main_entry_root, text="History", bootstyle="secondary", height=500, width=780)

        # Treeview (list box) with two columns
        self.treeview = ttk.Treeview(self.main_entry_label, columns=("Column 1", "Column 2", "Column 3", "Column 4"), show="headings")
        self.treeview.heading("Column 1", text="Time_stamp")
        self.treeview.heading("Column 2", text="Reference")
        self.treeview.heading("Column 3", text="Tags")
        self.treeview.heading("Column 4", text="Actions")

        # Adjust column widths based on content
        self.treeview.column("Column 1", width=200)  # Adjust width as needed
        self.treeview.column("Column 2", width=160)
        self.treeview.column("Column 3", width=200)
        self.treeview.column("Column 4", width=200)

        self.treeview.grid(row=0, column=1, padx=5, pady=5,  sticky="nsew")

        # Configure treeview to expand with the frame
        self.main_entry_label.grid_rowconfigure(0, weight=1)
        self.main_entry_label.grid_columnconfigure(0, weight=1)
        
        self.main_entry_label.pack(padx=5, pady=5, fill='both', expand=True)
        self.main_entry_root.place(relx=0.01, rely=0.3, relwidth=0.98, relheight=0.7)
        ###############################################################################


        ###############################################################################        
        # MAIN THREAD
        ###############################################################################
        # self.read_console_thread = threading.Thread(target=self.read_console)
        # self.read_console_thread.daemon = True
        # self.read_console_thread.start()
        ###############################################################################
        
                

    
    def get_theme_list(self, ttk_style):
        # Get the list of available themes from the ttkbootstrap module
        return ttk_style.theme_names()
    

    def apply_custom_styles(self):
        self.opr_btn_font = ttk.Style()
        self.opr_btn_style_type = "info.Link.TButton"
        self.opr_btn_font.configure(self.opr_btn_style_type, font=("Arial", 12))

        self.pop_btn_font = ttk.Style()
        self.pop_btn_style_type = "success.Link.TButton"
        self.pop_btn_font.configure(self.opr_btn_style_type, font=(12))


    def apply_theme(self, event):
        # Apply the selected theme
        selected_theme = self.theme_var.get()
        self.style.theme_use(selected_theme)
        self.apply_custom_styles()
        print(f"Theme '{selected_theme}' applied successfully!")


    def clear_all(self):
        pass


    def show_custom_message(self, value1, value2):
       custom_msg = ttk.Toplevel(root)
       custom_msg.title("Custom Message")
       custom_msg.geometry("300x200")  # Set custom size
       # Create a custom font for the message text
       custom_font = tkFont.Font(family="Arial", size=10)
       # Message content
       self.action_name = value1
       self.time_duration = value2
       message = f'''
            Name : {value1},
            Time : {value2} seconds
       '''
       # Label to display the message
       msg_label = ttk.Label(custom_msg, text=message, font=custom_font)
       msg_label.pack()
       # Button to close the custom message box
       close_button = ttk.Button(custom_msg, text="OK", command=custom_msg.destroy, bootstyle="success-link", style=self.pop_btn_style_type)
       close_button.pack(pady=10)


    def open_actions_popup(self, root, act_var, time_var):
        # CREATE WINDOW
        popup = ttk.Toplevel(root)
        popup.title("Actions")
        popup.geometry("400x200")

        # Entry fields
        entry1_label = ttk.Label(popup, text="Actions :")
        entry1_label.grid(row=0, column=0, pady=5, padx=10, stick="e")
        entry1 = ttk.Entry(popup, width=30)
        entry1.insert(0, "Entrance")
        entry1.grid(row=0, column=1, pady=5, padx=10, stick="w")
        
        entry2_label = ttk.Label(popup, text="Time duration :")
        entry2_label.grid(row=1, column=0, pady=5, padx=10, stick="e")
        entry2 = ttk.Entry(popup, width=8)
        entry2.insert(0, 5)
        entry2.grid(row=1, column=1, pady=5, padx=10, stick="w")
        label3 = ttk.Label(popup, text="seconds")
        label3.grid(row=1, column=1, padx=70, pady=10)

        # CHANGE VALUES OF ACTIONS VARIABLE
        def get_values():
           action = entry1.get()
           time_duration = entry2.get()
           act_var = action
           self.action_name = action
           self.time_duration = time_duration
           time_var = time_duration
           self.show_custom_message(act_var, time_var)
           popup.destroy()

        # Button to close the popup window
        close_button = ttk.Button(popup, text="Cancel", command=popup.destroy, bootstyle="success-link", style=self.pop_btn_style_type)
        close_button.grid(row=2, column=1, padx=10, pady=20, sticky='e')
        accept_button = ttk.Button(popup, text="Accept", command=get_values, bootstyle="success-link", style=self.pop_btn_style_type)
        accept_button.grid(row=2, column=2, padx=10, pady=20)


    def actions(self):
        self.open_actions_popup(self.root, self.action_name, self.time_duration)

    
    def open_tag_popup(self, root, csv_path):
        # CREATE WINDOW
        popup = ttk.Toplevel(root)
        popup.title("Tags")
        popup.geometry("500x400")

        # Treeview (list box) with two columns
        treeview = ttk.Treeview(popup, columns=("Column 1", "Column 2"), show="headings")
        treeview.heading("Column 1", text="Tags")
        treeview.heading("Column 2", text="References")
        treeview.grid(row=0, column=1, padx=5, pady=5)

        # CSV HANDLING
        if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
            df = pd.read_csv(csv_path, header=None)
            if not df.empty:
            # if df is not None:
                tag_name = df[0]
                ref_name = df[1]
                for i, j in zip(tag_name, ref_name):
                    treeview.insert('', 'end', values=(i, j))

        # Entry fields
        entry1_label = ttk.Label(popup, text="Tags :")
        entry1_label.grid(row=1, column=0, pady=5, padx=10, stick="e")
        entry1 = ttk.Entry(popup, width=30)
        entry1.grid(row=1, column=1, pady=5, padx=10, stick="w")
        
        entry2_label = ttk.Label(popup, text="References :")
        entry2_label.grid(row=2, column=0, pady=5, padx=10, stick="e")
        entry2 = ttk.Entry(popup, width=30)
        entry2.grid(row=2, column=1, pady=5, padx=10, stick="w")

        
        def update_list():
            all_data = {"tags" : [], "references": []}
            value1 = entry1.get()
            value2 = entry2.get()
            # Insert values into the listbox (Treeview)
            treeview.insert('', 'end', values=(value1, value2))
            entry1.delete(0, tk.END)
            entry2.delete(0, tk.END)
            all_data["tags"].append(value1)
            all_data["references"].append(value2)
            df = pd.DataFrame(all_data)
            if os.path.isfile(csv_path):
                df.to_csv(csv_path, mode='a', header=False, index=False)
            else:
                df.to_csv(csv_path, mode='w', header=False, index=False)

        
        def delete_selected():
            selected_item = treeview.selection()
            if selected_item:
                for item in selected_item:
                    treeview.delete(item)
                # Update the CSV file
                all_data = []
                for child in treeview.get_children():
                    all_data.append(treeview.item(child)["values"])
                df = pd.DataFrame(all_data, columns=["tags", "references"])
                df.to_csv(csv_path, mode='w', header=False, index=False)

        
        # BUTTON
        delete_button = ttk.Button(popup, text="Delete Entry", command=delete_selected, bootstyle="success-link", style=self.pop_btn_style_type)
        delete_button.grid(row=5, column=1, padx=5, pady=10)
        
        update_button = ttk.Button(popup, text="Update List", command=update_list, bootstyle="success-link", style=self.pop_btn_style_type)
        update_button.grid(row=5, column=1, padx=5, pady=10, sticky='e')

        close_button = ttk.Button(popup, text="Close", command=popup.destroy, bootstyle="success-link", style=self.pop_btn_style_type)
        close_button.grid(row=5, column=2, padx=10, pady=10, sticky='w')


    def tags(self):
        self.open_tag_popup(self.root, self.tags_details_csv)
    

    def __check_tag_details(self, tag_id, current_time):
        for tags in self.tags_details:
            if (tags['tag_id'] == tag_id):
                if (tags["last_updated_time"] > (current_time + datetime.timedelta(seconds=int(self.time_duration)))):
                    return True
                else:
                    return False
        else:
            return "Not Found!"
       
    
    def __update_tag_details(self, tag_id, current_time):
        for tags in self.tags_details:
            if (tags["tag_id"] == tag_id):
                tags["last_updated_time"] = current_time
                return True
        else:
            tag_details = {}
            tag_details["tag_id"] = tag_id
            tag_details["last_updated_time"] = current_time
            self.tags_details.append(tag_details)


    def __insert_into_treeview(self, time_stamp, references, tag):
        if self.action_name is not None:
            self.tree.insert("", tk.END, values=(time_stamp, references, tag, self.action_name))
        else:
            tk.messagebox.showerror("Error", "Please update action name first!")


    def read_console(self):
        self.reader.initialize_reader()
        self.reader.get_device_info()
        self.reader.get_all_params()
        self.reader.start_inventory()
        prev_val = 0
        # self.reader.start_scanning()
        try:
            while True:
                if self.reader.serial_port.in_waiting:
                    response = self.reader.serial_port.read(self.reader.serial_port.in_waiting)
                    print("Tag Read Response:", response)
                    if response is not None:
                        if len(response) > 26:
                            delimiter = b'\xcf'
                            split_bytes = response.split(delimiter)
                            split_segments = [delimiter + segment for segment in split_bytes if segment]
                            for i, segment in enumerate(split_segments):
                                tag_data = segment[-14:-2]
                                # tag_data = segment[-7:-2]
                                # if len(tag_data) > 5:
                                print(f"tag_data_len: {len(tag_data)}")
                                integer_value = int.from_bytes(tag_data, byteorder='big')
                                print(f"tag_data: {integer_value}")
                                ts = datetime.datetime.now()
                                ret = self.__check_tag_details(integer_value, ts)
                                print(f"ret: {ret}")
                                if ret==True or ret=="Not Found!":
                                    # ts = datetime.datetime.now()
                                    formatted_time = ts.strftime("%d/%m/%y, %H:%M")
                                    self.__insert_into_treeview(formatted_time, "pc 98", integer_value)
                                    self.__update_tag_details(integer_value, ts)
                                    print(self.tags_details)
                        self.get_data = True
                        if response[0] != 0xCF:
                            print("Invalid start byte")
                        tag_data = response[-14:-2]
                        # tag_data = response[-7:-2]
                        # if len(tag_data) > 5:
                        print(f"tag_data_len: {len(tag_data)}")
                        integer_value = int.from_bytes(tag_data, byteorder='big')  # or 'little' depending on your endianness
                        print(f"tag_data: {integer_value}")
                        ts = datetime.datetime.now()
                        ret = self.__check_tag_details(integer_value, ts)
                        print(f"ret: {ret}")
                        if ret==True or ret=="Not Found!":
                            # ts = datetime.datetime.now()
                            formatted_time = ts.strftime("%d/%m/%y, %H:%M")
                            self.__insert_into_treeview(formatted_time, "pc 98", integer_value)
                            self.__update_tag_details(integer_value, ts)
                            print(self.tags_details)
                time.sleep(0.1)
                # print(self.tags_details)
        except KeyboardInterrupt:
            self.reader.stop_inventory(self.reader.serial_port)
            print("Stopped inventory")

if __name__=="__main__":
    screen_resolution = [(m.width, m.height) for m in get_monitors()]
    # root = ttk.Window(title="orange@Accent-systems", size=screen_resolution[0])
    root = ttk.Window(title="orange@Accent-systems", size=(800, 480))
    app = Reader(root)
    root.mainloop()