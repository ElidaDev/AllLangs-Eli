import pyautogui
import keyboard
import time
from PIL import ImageGrab

clicktype = input("Left, Right or Middle click: ")
t = float(input("Wait time between clicks: "))  
m = float(input("Move to time: "))
times = int(input("Times to go through the loop: "))
a = int(input("Amount of times to click: "))
n = int(input("Amount of positions/images: "))
b = n
o = input("Images or Coords: ")
Images = []
xs = []
ys = []

if o == "Coords":
    while True:
        print("put Done when done with x positions")
        x = input("X's of locations: ")
        if x == "Done" :
            break
        else:
            xs.append(int(x))
    while True:
        print("put Done when done with y positions")
        y = input("Y's of locations: ")
        if y == "Done" :
            break
        else:
            ys.append(int(y))
    print(xs, ys)
    print(xs[1])
    for i in range(times):
        print ("Clicking...")
        n = b
        while n > 0:
            print(xs[n-1], ys[n-1])
            for i in range(a):
                pyautogui.moveTo(xs[n-1], ys[n-1], duration=m)
                time.sleep(t)
                if clicktype == "Left":
                    pyautogui.leftClick()
                elif clicktype == "Right":
                    pyautogui.rightClick()
                else:
                    pyautogui.middleClick()
                if keyboard.is_pressed('esc'):
                    break
            n = n-1
            if keyboard.is_pressed('esc'):
                break
elif o == "Images":
    while True:
        print("Make sure to put the .png or .jpg at the end also, put Done when done with images.")
        c = input ("Inputimages: ")
        if c == "Done":
            break
        else:
            Images.append(c)
    print("Waiting to start...")
    time.sleep(5)
    print("Starting...")
    time.sleep(0.5)
    if clicktype == "Left":
        while n > 0:
            print(Images[n-1])
            location = pyautogui.locateCenterOnScreen(Images[n-1], confidence=0.75)
            if location is not None:
                x, y = location
                for i in range(a):    
                    pyautogui.moveTo(x, y, duration=m)
                    time.sleep(t)
                    if clicktype == "Left":
                        pyautogui.leftClick(x,y)
                    elif clicktype == "Right":
                        pyautogui.rightClick(x,y)
                    else:
                        pyautogui.middleClick(x,y)
                    print(x, y)
                    time.sleep(2)
                    if keyboard.is_pressed('esc'):
                        break
                n=n-1
                if keyboard.is_pressed('esc'):
                    break
            else:
                print("Image not found!")
   