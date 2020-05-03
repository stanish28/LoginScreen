

import tkinter as tk
window = tk.Tk()
window.title("GUI")
window.geometry('350x350')
label = tk.Label(window, text = "USERNAME", font = "ArialBond").place(x=15,y=45)
label1 = tk.Label(window, text = "PASSWORD", font = "ArialBond").place(x=15,y=85)
sumbit = tk.Button(window, text = "SUMBIT", fg="RED", bg="Blue").place(x=15,y=125)
entry  = tk.Entry(window, width=10).place(x=95,y=45)
entry1 = tk.Entry(window, width=10).place(x=95,y=85)
window.mainloop()






"""
from tkinter import *  
  
top = Tk()  
  
top.geometry("400x250")  
  
#creating label  
uname = Label(top, text = "Username").place(x = 30,y = 50) 
top.mainloop() 
"""