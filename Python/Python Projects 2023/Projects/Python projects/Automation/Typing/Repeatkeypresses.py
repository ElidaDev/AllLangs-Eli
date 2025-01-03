import time
import keyboard


p = input("Key: ")
t = int(input("Amount of times to repeat: "))
w = float(input("Wait between typing: "))

time.sleep(10) # wait before running to allow switching screens and other things...
for i in range(t):
    keyboard.press_and_release(p)
    time.sleep(w)
    if keyboard.is_pressed('esc'):
        break