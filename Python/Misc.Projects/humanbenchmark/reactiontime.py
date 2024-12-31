import pyautogui as pag
import time
import keyboard 

time.sleep(10)
while True:
    if pag.pixelMatchesColor(1245, 401, [75, 219, 106]):
        pag.click(1245,401)
    if pag.pixelMatchesColor(1245, 401, [43, 135, 209]):
        pag.click(1245,401)
    if keyboard.is_pressed('q'):
        break