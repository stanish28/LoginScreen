import tkinter as tk
window = tk.Tk()
window.title("FUNCTIONS")
window.geometry("350x350")
def clicked():
    print("hello")
bt = tk.Button(window, text="clicked",command=clicked)
bt.grid(column=0, row=1)
window.mainloop()