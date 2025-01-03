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
    for z in range(t):
        time.sleep(s)
        if c == "Left":
            pyautogui.leftClick(x,y)
        elif c == "Right":
            pyautogui.rightClick(x,y)
        else:
            pyautogui.middleClick(x,y)
        if keyboard.is_pressed('esc'):
            break
elif coords == "n":
    time.sleep(z)
    for z in range(t):
        time.sleep(s)
        if c == "Left":
            pyautogui.leftClick()
        elif c == "Right":
            pyautogui.rightClick()
        else:
            pyautogui.middleClick()
        if keyboard.is_pressed('esc'):
            break


