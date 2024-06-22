import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


# root = tk.Tk()      # tk-inter style

# root = ttk.Window(themename="darkly")
root = ttk.Window()


#####################################################################################################
# BUTTON
#####################################################################################################
'''
bootstyle type : "info-outline", "infooutline", "info outline", "outline-info", ("info", "outline"), (INFO, OUTLINE)
'''

# b1 = ttk.Button(root, text='Solid-btn', bootstyle=SUCCESS)
# b1.pack(side=LEFT, padx=5, pady=10)

# b2 = ttk.Button(root, text="Outline-btn", bootstyle=(INFO, OUTLINE))
# b2.pack(side=LEFT, padx=5, pady=10)

# b3 = ttk.Button(root, text="Link-btn", bootstyle=(INFO, LINK))
# b3.pack(side=LEFT, padx=5, pady=10)

# b4 = ttk.Button(root, text="Disabled", bootstyle=DANGER, state=DISABLED)
# b4.pack(side=LEFT, padx=5, pady=10)


# OUTLINE BUTTON
# for color in root.style.colors:
#     b = ttk.Button(root, text=color, bootstyle=(color, OUTLINE))
#     b.pack(side=LEFT, padx=5, pady=5)
#     b1 = ttk.Button(root, text=color, bootstyle=color)
#     b1.pack(side=LEFT, padx=5, pady=5)


# LINK BUTTON
# for color in root.style.colors:
#     b = ttk.Button(root, text=color, bootstyle=(color, LINK))
#     b.pack(side=LEFT, padx=5, pady=10)


# CHECK BUTTON
# for color in root.style.colors:
#     b = ttk.Checkbutton(root, text=color, bootstyle=color)
#     b.pack(side=LEFT, padx=5, pady=10)


# CHECKBUTTON - TOOL, OUTLINE
# for color in root.style.colors:
#     b = ttk.Checkbutton(root, text=color, bootstyle=(color, TOOLBUTTON, OUTLINE))
#     b.pack(side=LEFT, padx=5, pady=10)


# CHECKBUTTON - ROUND TOGGLE, SQUARE-TOGGLE, DISABLED
# for color in root.style.colors:
#     # b = ttk.Checkbutton(root, text=color, bootstyle=(color, "round-toggle"))
#     b = ttk.Checkbutton(root, text=color, bootstyle=(color, "square-toggle"))
#     # b = ttk.Checkbutton(root, text=color, bootstyle=(color, "square-toggle"), state=DISABLED)
#     b.pack(side=LEFT, padx=5, pady=10)


#####################################################################################################



#####################################################################################################
# COMBOBOX
#####################################################################################################

# for color in root.style.colors:
#     c = ttk.Combobox(root, text=color, bootstyle=color, state=READONLY)
#     c.pack(side=LEFT, padx=5, pady=10)

#####################################################################################################



#####################################################################################################
# DATE-ENTRY
#####################################################################################################

# for color in root.style.colors:
#     d = ttk.DateEntry(root, bootstyle=color)
#     d.pack(side=LEFT, padx=5, pady=10)


# DATE PICKUP POPUP
# for color in root.style.colors:
#     d = ttk.DatePickerPopup(root, bootstyle=INFO)
#     d.pack(side=LEFT, padx=5, pady=10)

#####################################################################################################



#####################################################################################################
#
#####################################################################################################



#####################################################################################################



#####################################################################################################
#
#####################################################################################################



#####################################################################################################
root.mainloop()