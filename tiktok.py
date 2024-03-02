from time import strftime #call time func
from tkinter import *  #gui interface 
from tkinter.ttk import * #gui theme
import pytz #deals with timezone definitions
from datetime import datetime  #deals with date and time manipulations
table = Tk()  # creating window 
table.title("Tikety-tokety") # naming the window 


def time():
    CETtime = pytz.timezone('Europe/Brussels')
    getCETtime = datetime.now(CETtime)
    table =  getCETtime.strftime("%H:%M:%S %p") #strftime is used to format how the time will be displayed
    lbl.config(text=table) 
    lbl.after(1000, time)

lbl = Label(table, font = ("droid serif" , 40 ,"bold" ),
           background= 'dark blue', foreground= "white" )
Label(table,text='CET time' ).pack()
lbl.pack(anchor= "center") #must be n, ne, e, se, s, sw, w, nw, or center
time()
mainloop()
