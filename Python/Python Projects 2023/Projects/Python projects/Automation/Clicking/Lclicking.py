import pyautogui
import time
import keyboard
z = int(input("Wait before start: "))
c = input("Left Middle or Right click: ")
coords = input("Do you know the coordinates: y/n ")
t = int(input("Amount of clicks: "))
s = float(input("Wait in seconds: "))

if coords == "y":
    x = int(input("X-Coordinate: "))
    y = int(input("Y-Coordinate: "))
    
    time.sleep(z)
    pyautogui.moveTo(x, y, duration=5)
    if c == "Left":
        for z in range(t):
            time.sleep(s)
            pyautogui.leftClick(x, y)
            if keyboard.is_pressed('esc'):
                break
    elif c == "Right":
        for z in range(t):
            time.sleep(s)
            pyautogui.rightClick(x, y)
            if keyboard.is_pressed('esc'):
                break
    elif c == "Middle":
        for z in range(t):
            time.sleep(s)
            pyautogui.middleClick(x, y)
            if keyboard.is_pressed('esc'):
                break
    else: 
        print("Incorrect input")
elif coords == "n":
    time.sleep(z)
    if c == "Left":
        for z in range(t):
            time.sleep(s)
            pyautogui.leftClick()
            if keyboard.is_pressed('esc'):
                break
    elif c == "Right":
        for z in range(t):
            time.sleep(s)
            pyautogui.rightClick()
            if keyboard.is_pressed('esc'):
                break
    elif c == "Middle":
        for z in range(t):
            time.sleep(s)
            pyautogui.middleClick()
            if keyboard.is_pressed('esc'):
                break
    else: 
        print("Incorrect input")


