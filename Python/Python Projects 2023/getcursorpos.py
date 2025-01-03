import pyautogui as pag
import keyboard
import time

print("Press 'v' to print the position of your cursor to the console!")
while True:
    time.sleep(1)
    if keyboard.is_pressed('v'):
        print(pag.position())
    if keyboard.is_pressed('q'):
        break