#Trying to brute force button on DZ


import keyboard
import pyautogui
import time
while True:    
    if keyboard.is_pressed('q'):
        for _ in range(15):
            pyautogui.mouseDown(duration=0.04,button='right')    
            pyautogui.mouseDown(duration=0.05,button='left')
            pyautogui.mouseDown(duration=0.04,button='right') 
            pyautogui.mouseUp(duration=0.005,button='right')
            pyautogui.mouseUp(duration=0.005,button='left')
            
