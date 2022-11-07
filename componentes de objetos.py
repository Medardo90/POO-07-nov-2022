# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:23:04 2022

@author: lab
"""

#componomtes de objetos

import tkinter as tk
from tkinter import ttk

# root window
root=tk.Tk()
root.geometry("240x100")
root.title("login")
root.resizable(0,0)
 #CONFIGURE THE GRID
 
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

#useername 
username_label=ttk.Label(root, text="Username:")
username_label.grid(column=1,row=0, sticky= tk.E ,padx=5, pady=5)

username_entry= ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky= tk.E ,padx=5, pady=5)
#pasaword

password_label= ttk.Label(root,text="Password")
password_label.grid(column=0, row=1, sticky= tk.W, padx=5, pady=5)

password_entry =ttk.Entry(root, show="------")
password_entry.grid(column=1, row=1, sticky= tk.E, padx=5, pady=5)

#login button 
login_button= ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, sticky= tk.E, padx=5, pady=5)

root.mainloop()
 