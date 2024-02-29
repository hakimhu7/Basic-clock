from time import strftime #call time func
from tkinter import *  #gui interface 
from tkinter.ttk import * #gui theme
import pytz
from datetime import datetime
table = Tk()  # creating window 
table.title("Amina's tikety-tokety") # naming the window 

def time():
    kazakhtime = pytz.timezone('Etc/GMT+6')
    getkazakhtime = datetime.now(kazakhtime)
    table =  getkazakhtime.strftime("%H:%M:%S %p" ) #strftime is used to format how the time will be displayed
    lbl.config(text=table) 
    lbl.after(1000, time)

lbl = Label(table, font = ("gothic" , 40 ,"bold" ),
           background= 'dark blue', foreground= "white" )

lbl.pack(anchor= "center") #must be n, ne, e, se, s, sw, w, nw, or center
time()
mainloop()

