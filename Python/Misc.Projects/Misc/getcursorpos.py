import pyautogui as pag
import keyboard
import time

while True:
    time.sleep(1)
    if keyboard.is_pressed('v'):
        print(pag.position())
    if keyboard.is_pressed('q'):
        break