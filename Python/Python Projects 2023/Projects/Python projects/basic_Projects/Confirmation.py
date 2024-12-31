import tkinter as tk
from tkinter import ttk
import os

global SELECTED
SELECTED = False
global Application
Application = 404
global Active
Active = True
while Active == True:
    if Application == 404:    
        global OPTIONSELECTOR
        class App1():
            def __init__(self):
                self.root = tk.Tk()#making the app
                self.root.geometry('450x250')#making the app
                self.root.title('Eli''s application launcher')#making the title
                self.mainframe = tk.Frame(self.root)#making the app
                self.mainframe.pack(fill='both', expand='true')#making the app
                set_1_button = ttk.Button(self.mainframe, text='My Python Applications', command=self.o1)#widget
                set_1_button.grid(row=2, column=0, pady=5, padx=5,)#widget
                set_3_button = ttk.Button(self.mainframe, text='Other applications', command=self.o2)#widget
                set_3_button.grid(row=2, column=2, pady=5, padx=5,)#widget
                set_2_button = ttk.Button(self.mainframe, text='Calculations in py', command=self.o3)#widget
                set_2_button.grid(row=2, column=1, pady=5, padx=5,)#widget
                set_ext_button = ttk.Button(self.mainframe, text='Exit', command=self.ext)#widget
                set_ext_button.grid(row=3, column=3, pady=5, padx=5,)#widget
                self.root.mainloop()
                return
            def o1(self):
                print("My python!")
                global OPTIONSELECTOR
                global SELECTED
                OPTIONSELECTOR = "Python"
                SELECTED = True
            def o2(self):
                print("NOT MINE!")
                global OPTIONSELECTOR
                global SELECTED
                OPTIONSELECTOR = "NM"
                SELECTED = True
            def o3(self):
                print("Calculators in py")
                global OPTIONSELECTOR
                global SELECTED
                OPTIONSELECTOR = "Calcpy"
                SELECTED = True
            def ext(self):
                print("Exit")
                global Active
                Active = False
                self.root.destroy()
        if Active == False:
            break        
        if SELECTED == False:
            if Active == True:
                print("Entering application due to Selected being False")
                App1()
        if OPTIONSELECTOR == "Python":        
            class App2():
                def __init__(self):
                    self.root = tk.Tk()#making the app
                    self.root.geometry('450x250')#making the app
                    self.root.title('Eli''s application launcher')#making the title
                    self.mainframe = tk.Frame(self.root)#making the app
                    self.mainframe.pack(fill='both', expand='true')#making the app
                    set_1_button = ttk.Button(self.mainframe, text='Countdown', command=self.Con1)#widget
                    set_1_button.grid(row=2, column=0, pady=5, padx=5,)#widget
                    set_2_button = ttk.Button(self.mainframe, text='AntiAfk', command=self.Con2)#widget
                    set_2_button.grid(row=2, column=1, pady=5, padx=5,)#widget
                    set_3_button = ttk.Button(self.mainframe, text='Calculator', command=self.Con3)#widget
                    set_3_button.grid(row=2, column=2, pady=5, padx=5,)#widget
                    set_4_button = ttk.Button(self.mainframe, text='Cardpicker', command=self.Con4)#widget
                    set_4_button.grid(row=2, column=3, pady=5, padx=5,)#widget
                    set_5_button = ttk.Button(self.mainframe, text='Dice', command=self.Con5)#widget
                    set_5_button.grid(row=3, column=0, pady=5, padx=5,)#widget
                    set_6_button = ttk.Button(self.mainframe, text='Random String', command=self.Con6)#widget
                    set_6_button.grid(row=3, column=1, pady=5, padx=5,)#widget
                    set_7_button = ttk.Button(self.mainframe, text='Brute', command=self.Con7)#widget
                    set_7_button.grid(row=3, column=2, pady=5, padx=5,)#widget
                    set_8_button = ttk.Button(self.mainframe, text='Numbers in range', command=self.Con8)#widget
                    set_8_button.grid(row=3, column=3, pady=5, padx=5,)#widget
                    set_9_button = ttk.Button(self.mainframe, text='Repeatwrite', command=self.Con9)#widget
                    set_9_button.grid(row=4, column=0, pady=5, padx=5,)#widget
                    set_10_button = ttk.Button(self.mainframe, text='Clicking', command=self.Con10)#widget
                    set_10_button.grid(row=4, column=1, pady=5, padx=5,)#widget
                    set_11_button = ttk.Button(self.mainframe, text='Coinflip', command=self.Con11)#widget
                    set_11_button.grid(row=4, column=2, pady=5, padx=5,)#widget
                    set_12_button = ttk.Button(self.mainframe, text='Cursor position (v)', command=self.Con12)#widget
                    set_12_button.grid(row=4, column=3, pady=5, padx=5,)#widget
                    set_13_button = ttk.Button(self.mainframe, text='Multi Loc clicking', command=self.Con13)#widget
                    set_13_button.grid(row=5, column=0, pady=5, padx=5,)#widget
                    set_Final_button = ttk.Button(self.mainframe, text='Back', command=self.back)#widget
                    set_Final_button.grid(row=5, column=3, pady=5, padx=5,)#widget
                    self.root.mainloop()
                    return
                def back(self):
                    global Application
                    global SELECTED
                    Application = 404
                    SELECTED = False
                def Con1(self):
                    global Application
                    Application = 0
                    print(Application)
                def Con2(self):
                    global Application
                    Application = 1
                    print(Application)
                def Con3(self):
                    global Application
                    Application = 2
                    print(Application)
                def Con4(self):
                    global Application
                    Application = 3
                    print(Application)
                def Con5(self):
                    global Application
                    Application = 4
                    print(Application)
                def Con6(self):
                    global Application
                    Application = 5
                    print(Application)
                def Con7(self):
                    global Application
                    Application = 6
                    print(Application)
                def Con8(self):
                    global Application
                    Application = 7
                    print(Application)
                def Con9(self):
                    global Application
                    Application = 8
                    print(Application)
                def Con10(self):
                    global Application
                    Application = 9
                    print(Application)
                def Con11(self):
                    global Application
                    Application = 10
                    print(Application)
                def Con12(self):
                    global Application
                    Application = 11
                    print(Application)
                def Con13(self):
                    global Application
                    Application = 12
                    print(Application)            
        if OPTIONSELECTOR == "NM":
            class App2():
                def __init__(self):
                    global Application
                    Application = 404
                    self.root = tk.Tk()#making the app
                    self.root.geometry('450x250')#making the app
                    self.root.title('Eli''s application launcher')#making the title
                    self.mainframe = tk.Frame(self.root)#making the app
                    self.mainframe.pack(fill='both', expand='true')#making the app
                    set_1_button = ttk.Button(self.mainframe, text='Minecraft', command=self.Con1)#widget
                    set_1_button.grid(row=1, column=0, pady=5, padx=5,)#widget
                    set_2_button = ttk.Button(self.mainframe, text='Steam', command=self.Con2)#widget
                    set_2_button.grid(row=1, column=1, pady=5, padx=5,)#widget
                    set_3_button = ttk.Button(self.mainframe, text='Discord', command=self.Con3)#widget
                    set_3_button.grid(row=1, column=2, pady=5, padx=5,)#widget
                    set_4_button = ttk.Button(self.mainframe, text='Keypad Software', command=self.Con4)#widget
                    set_4_button.grid(row=1, column=3, pady=5, padx=5,)#widget
                    set_5_button = ttk.Button(self.mainframe, text='Roblox', command=self.Con5)#widget
                    set_5_button.grid(row=2, column=0, pady=5, padx=5,)#widget
                    set_6_button = ttk.Button(self.mainframe, text='CMD', command=self.Con6)#widget
                    set_6_button.grid(row=2, column=1, pady=5, padx=5,)#widget
                    set_Final_button = ttk.Button(self.mainframe, text='Back', command=self.back)#widget
                    set_Final_button.grid(row=5, column=3, pady=5, padx=5,)#widget
                    self.root.mainloop()
                    return
                def back(self):
                    global Application
                    global SELECTED
                    Application = 404
                    SELECTED = False
                def Con1(self):
                    global Application
                    Application = 0
                    print(Application)
                def Con2(self):
                    global Application
                    Application = 1
                    print(Application)
                def Con3(self):
                    global Application
                    Application = 2
                    print(Application)
                def Con4(self):
                    global Application
                    Application = 3
                    print(Application)   
                def Con5(self):
                    global Application
                    Application = 4
                    print(Application)   
                def Con6(self):
                    global Application
                    Application = 5
                    print(Application)
        if OPTIONSELECTOR == "Calcpy":
            class App2():
                def __init__(self):
                    global Application
                    Application = 404
                    self.root = tk.Tk()#making the app
                    self.root.geometry('450x250')#making the app
                    self.root.title('Eli''s application launcher')#making the title
                    self.mainframe = tk.Frame(self.root)#making the app
                    self.mainframe.pack(fill='both', expand='true')#making the app
                    set_1_button = ttk.Button(self.mainframe, text='Convertor', command=self.Con1)#widget
                    set_1_button.grid(row=1, column=0, pady=5, padx=5,)#widget
                    set_2_button = ttk.Button(self.mainframe, text='Average', command=self.Con2)#widget
                    set_2_button.grid(row=1, column=1, pady=5, padx=5,)#widget
                    set_3_button = ttk.Button(self.mainframe, text='WIP', command=self.Con3)#widget
                    set_3_button.grid(row=1, column=2, pady=5, padx=5,)#widget
                    set_4_button = ttk.Button(self.mainframe, text='WIP', command=self.Con4)#widget
                    set_4_button.grid(row=1, column=3, pady=5, padx=5,)#widget
                    set_5_button = ttk.Button(self.mainframe, text='WIP', command=self.Con5)#widget
                    set_5_button.grid(row=2, column=0, pady=5, padx=5,)#widget
                    set_6_button = ttk.Button(self.mainframe, text='WIP', command=self.Con6)#widget
                    set_6_button.grid(row=2, column=1, pady=5, padx=5,)#widget
                    set_Final_button = ttk.Button(self.mainframe, text='Back', command=self.back)#widget
                    set_Final_button.grid(row=5, column=3, pady=5, padx=5,)#widget
                    self.root.mainloop()
                    return
                def back(self):
                    global Application
                    global SELECTED
                    Application = 404
                    SELECTED = False
                def Con1(self):
                    global Application
                    Application = 0
                    print(Application)
                def Con2(self):
                    global Application
                    Application = 1
                    print(Application)
                def Con3(self):
                    global Application
                    Application = 2
                    print(Application)
                def Con4(self):
                    global Application
                    Application = 3
                    print(Application)   
                def Con5(self):
                    global Application
                    Application = 4
                    print(Application)   
                def Con6(self):
                    global Application
                    Application = 5
                    print(Application)
        App2()
    if Application != 404:
        break

if Application != 404:
    ApplicationsP = ["C:/Users/elija/Desktop/Python Projects 2023/Projects/Python projects/basic_Projects/Countdown.py","C:/Users/elija/Desktop/Python Projects 2023/Projects/Python projects/basic_Projects/antiAfk.py", "C:/Users/elija/Desktop/Python Projects 2023/Projects/Python projects/basic_Projects/Calc.py", "C:/Users/elija/Desktop/Python Projects 2023/Projects/Python projects/basic_Projects/Cardpicker.py", "C:/Users/elija/Desktop/Python Projects 2023/Projects/Python projects/basic_Projects/Diceroll.py", "C:/Users/elija/Desktop/Python Projects 2023/Projects/Python projects/basic_Projects/StringGen.py", "C:/Users/elija/Desktop/Python Projects 2023/Projects/Python projects/Automation/brute.py", "C:/Users/elija/Desktop/Python Projects 2023/Projects/Python projects/Automation/Typing/numbers.py", "C:/Users/elija/Desktop/Python Projects 2023/Projects/Python projects/Automation/Typing/Repeatwrite.py", "C:/Users/elija/Desktop/Python Projects 2023/Projects/Python projects/Automation/Clicking/Lclicking.py", "C:/Users/elija/Desktop/Python Projects 2023/Projects/Python projects/basic_Projects/Coinflip.py", "C:/Users/elija/Desktop/Python Projects 2023/Projects/Python projects/basic_Projects/getcursorpos.py", "C:/Users/elija/Desktop/Python Projects 2023/Projects/Python projects/Automation/Clicking/Clicktheimagesorpositions.py"]
    ApplicationsNM = ["C:/ProgramData\Microsoft/Windows/Start Menu/Programs/Minecraft Launcher/Minecraft Launcher.lnk", "C:/Users/elija/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Steam/Steam.lnk", "C:/Users/elija/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Discord Inc/Discord.lnk", "C:/Users/Public/Desktop/Glorious Core.lnk", "C:/Users/elija/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Roblox/Roblox Player.lnk", "C:/Users/elija/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/System Tools/Command Prompt.lnk"]
    Applicationscalc = ["C:/Users/elija/Desktop/Python Projects 2023/Projects/Python projects/basic_Projects/MultiConverter.py", "C:/Users/elija/Desktop/Python Projects 2023/Projects/Python projects/basic_Projects/Average.py"]
    if OPTIONSELECTOR == "Python":
        os.startfile(ApplicationsP[Application])
    if OPTIONSELECTOR == "NM":
        os.startfile(ApplicationsNM[Application])
    if OPTIONSELECTOR == "Calcpy":
        os.startfile(Applicationscalc[Application])
else:
    print("Something went wrong! (404)")