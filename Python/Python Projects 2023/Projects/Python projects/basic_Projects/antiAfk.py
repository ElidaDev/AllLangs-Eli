import pyautogui as pag
import random as rdm
import time
import keyboard as kbrd
import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        self.root = tk.Tk()#making the app
        self.root.geometry('450x300')#making the app
        self.root.title('ANTI AFK')#making the title
        self.mainframe = tk.Frame(self.root)#making the app
        self.mainframe.pack(fill='both', expand='true')#making the app
        self.text = ttk.Label(self.mainframe, text='ANTI AFK', font=('brass mono', 30))#making the app
        self.text.grid(row=0,column=0)#making the app
        self.set_wait = ttk.Entry(self.mainframe, )#widget
        self.set_wait.grid(row=1, column=0, pady=10, padx=10, sticky='nwes')#widget
        set_wait_button = ttk.Button(self.mainframe, text='Set wait time', command=self.setWait)#widget
        set_wait_button.grid(row=1, column=1, pady=10, padx=10)#widget
        self.set_afkt = ttk.Entry(self.mainframe, )#widget
        self.set_afkt.grid(row=2, column=0, pady=10, padx=10, sticky='nwes')#widget
        set_afkt_button = ttk.Button(self.mainframe, text='Set away time', command=self.setafkTime)#widget
        set_afkt_button.grid(row=2, column=1, pady=10, padx=10)#widget
        self.set_mtt = ttk.Entry(self.mainframe, )#widget
        self.set_mtt.grid(row=3, column=0, pady=10, padx=10, sticky='nwes')#widget
        set_mtt_button = ttk.Button(self.mainframe, text='Set moveto time', command=self.setMoveTo)#widget
        set_mtt_button.grid(row=3, column=1, pady=10, padx=10)#widget
        self.set_c = ttk.Entry(self.mainframe, )#widget
        self.set_c.grid(row=4, column=0, pady=10, padx=10, sticky='nwes')#widget
        set_c_button = ttk.Button(self.mainframe, text='Click> True or False', command=self.setclickbool)#widget
        set_c_button.grid(row=4, column=1, pady=10, padx=10)#widget
        self.start = ttk.Entry(self.mainframe, )#widget
        self.start.grid(row=5, column=0, pady=10, padx=10, sticky='nwes')#widget
        set_start_button = ttk.Button(self.mainframe, text='Start?> True or False', command=self.starta)#widget
        set_start_button.grid(row=5, column=1, pady=10, padx=10)#widget
        self.root.mainloop()
        return
    def setWait(self):
        try:
            global wait
            wait = int(self.set_wait.get())
            print(wait)
            return wait
        except ValueError:
            print("Enter a valid number")
    def setafkTime(self):
        try:
            global afkTime
            afkTime = int(self.set_afkt.get())
            print(afkTime)
            return afkTime
        except ValueError:
            print("Enter a valid number")
    def setMoveTo(self):
        try:
            global moveTo
            moveTo = int(self.set_mtt.get())
            print(moveTo)
            return moveTo
        except ValueError:
            print("Enter a valid number")
    def setclickbool(self):
        try:
            global click
            click = bool(self.set_c.get())
            print(click)
            return click
        except ValueError:
            print("Enter a valid input 'True', or 'False' ")
    def starta(self):
        try:
            global start_sc
            start_sc = bool(self.set_c.get())
            print(start_sc)
            return start_sc
        except ValueError:
            print("Enter a valid input 'True', or 'False' ") 

App()    
time.sleep(5)
if start_sc == True:
    while afkTime >= 0:
        print("Hold escape to exit!")
        if kbrd.is_pressed("esc"):
            break
        time.sleep(wait)
        afkTime = (afkTime - wait) - moveTo
        x = rdm.randint(500, 800)
        y = rdm.randint(500, 800)
        pag.moveTo(x, y, moveTo)
        if kbrd.is_pressed("esc"):
            break
        if click == "y":
            pag.click()