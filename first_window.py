from tkinter import *
from tkinter import ttk

mywindow = Tk()
mywindow.title("My app")
mywindow.geometry("800x600")
frm=ttk.Frame(mywindow, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

mywindow.mainloop()
