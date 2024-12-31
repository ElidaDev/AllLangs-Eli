import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        self.root = tk.Tk()#making the app
        self.root.geometry('350x200')#making the app
        self.root.title('Application')#making the title
        self.mainframe = tk.Frame(self.root)#making the app
        self.mainframe.pack(fill='both', expand='true')#making the app
        self.text = ttk.Label(self.mainframe, text='Testing', font=('brass mono', 30))#making the app
        self.text.grid(row=0,column=0)#making the app
        self.set_wait = ttk.Entry(self.mainframe, )#widget
        self.set_wait.grid(row=1, column=0, pady=10, sticky='nwes')#widget
        set_wait_button = ttk.Button(self.mainframe, text='Set wait time', command=self.setWait)#widget
        set_wait_button.grid(row=1, column=1, pady=10)#widget
        self.root.mainloop()
        return

    def setWait(self):
        try:
            wait = int(self.set_wait.get())
            print(wait)
        except ValueError:
            print("Enter a valid number")
        
App()