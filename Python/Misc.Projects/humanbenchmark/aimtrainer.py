import pyautogui as p
import keyboard

while True:
    if keyboard.is_pressed('q'):
        break
    a = 0
    b = 0
    while(a==0 and b==0):
        try:
            a,b = p.locateCenterOnScreen("Target.JPG",confidence=0.7, grayscale=True, region=(290,140,780,300))
        except TypeError:
            pass
    if keyboard.is_pressed('q'):
        break
    p.click(a,b)
    