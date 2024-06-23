

###### change labelframe bg color

# import tkinter as tk
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *

# def change_bg_color():
#     style.configure('Custom.TLabelframe', background='#ADD8E6')  # Light Blue color
#     label_frame.configure(style='Custom.TLabelframe')

# root = ttk.Window(themename="flatly")

# # Create a style object
# style = ttk.Style()

# # Create a LabelFrame
# label_frame = ttk.LabelFrame(root, text="My Label Frame", width=200, height=100)
# label_frame.pack(pady=20, padx=20)

# # Create a Button to change the background color
# change_color_button = ttk.Button(root, text="Change Background Color", command=change_bg_color)
# change_color_button.pack(pady=10)

# root.mainloop()



####################### popup window



# import tkinter as tk
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *


# class MainApp(ttk.Window):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         # Main window settings
#         self.title("Main Window")
#         self.geometry("800x600")
        
#         # Button to open the popup
#         self.open_popup_button = ttk.Button(self, text="Open Popup", command=self.open_popup)
#         self.open_popup_button.pack(pady=20)

#     def open_popup(self):
#         # Create the popup window
#         self.popup = ttk.Toplevel(self)
#         self.popup.title("Popup Window")
#         self.popup.geometry("400x300")

#         # Treeview (list box) with two columns
#         self.treeview = ttk.Treeview(self.popup, columns=("Column 1", "Column 2"), show="headings")
#         self.treeview.heading("Column 1", text="Column 1")
#         self.treeview.heading("Column 2", text="Column 2")
#         self.treeview.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

#         # Entry fields
#         self.entry1 = ttk.Entry(self.popup)
#         self.entry2 = ttk.Entry(self.popup)
#         self.entry1.pack(pady=5, padx=10)
#         self.entry2.pack(pady=5, padx=10)

#         # Buttons for update and cancel
#         self.update_button = ttk.Button(self.popup, text="Update", command=self.update_list)
#         self.cancel_button = ttk.Button(self.popup, text="Cancel", command=self.popup.destroy)
#         self.update_button.pack(side=tk.LEFT, padx=10, pady=10)
#         self.cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

#     def update_list(self):
#         # Get the values from the entry fields
#         value1 = self.entry1.get()
#         value2 = self.entry2.get()

#         # Insert the values into the treeview
#         self.treeview.insert('', 'end', values=(value1, value2))

#         # Clear the entry fields
#         self.entry1.delete(0, tk.END)
#         self.entry2.delete(0, tk.END)


# if __name__ == "__main__":
#     app = MainApp(themename="minty")
#     app.mainloop()


############ popup with label on entry field

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class MainApp(ttk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Main window settings
        self.title("Main Window")
        self.geometry("800x600")
        
        # Button to open the popup
        self.open_popup_button = ttk.Button(self, text="Open Popup", command=self.open_popup)
        self.open_popup_button.pack(pady=20)

    def open_popup(self):
        # Create the popup window
        self.popup = ttk.Toplevel(self)
        self.popup.title("Popup Window")
        self.popup.geometry("400x300")

        # Treeview (list box) with two columns
        self.treeview = ttk.Treeview(self.popup, columns=("Column 1", "Column 2"), show="headings")
        self.treeview.heading("Column 1", text="Column 1")
        self.treeview.heading("Column 2", text="Column 2")
        self.treeview.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

        # Labels and Entry fields in a grid layout
        self.label1 = ttk.Label(self.popup, text="Input 1:")
        self.entry1 = ttk.Entry(self.popup)
        self.label2 = ttk.Label(self.popup, text="Input 2:")
        self.entry2 = ttk.Entry(self.popup)
        
        self.label1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry1.grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)
        self.label2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry2.grid(row=1, column=1, padx=10, pady=5, sticky=tk.EW)

        self.popup.grid_columnconfigure(1, weight=1)  # Make the second column expandable

        # Buttons for update and cancel
        self.update_button = ttk.Button(self.popup, text="Update", command=self.update_list)
        self.cancel_button = ttk.Button(self.popup, text="Cancel", command=self.popup.destroy)
        self.update_button.grid(row=2, column=0, padx=10, pady=10)
        self.cancel_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

    def update_list(self):
        # Get the values from the entry fields
        value1 = self.entry1.get()
        value2 = self.entry2.get()

        # Insert the values into the treeview
        self.treeview.insert('', 'end', values=(value1, value2))

        # Clear the entry fields
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)


if __name__ == "__main__":
    app = MainApp(themename="minty")
    app.mainloop()
