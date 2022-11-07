# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:14:13 2022

@author: lab
"""

from tkinter import *  #doble clic en tkimter y contrl g sale la libreria de ttk
window= Tk()
window.geometry("400x200")
window.title("ejemplo place()")

button1 = Button(window, text="H=100 W=100")
button1.place(height= 100, width= 100)

button2 = Button(window, text="X=100 RH=0.2 RW=0.2 ")
button2.place(x=100, relheight=0.2, relwidth=0.2)

button3 = Button(window, text="X=500, Y=250 ")
button3.place(x=500, y=250)

button4 = Button(window, text="relx=0.4 rely=0.3 ")
button4.place(relx=0.4, rely=0.3)

button5 = Button(window, text="bordermode = INSIDE ")
button5.place(x=350,bordermode = INSIDE )

window.mainloop()