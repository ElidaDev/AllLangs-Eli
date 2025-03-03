import pyautogui as pag
import keyboard as kbrd
import time
import itertools

passw = 1234
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
digits = int(input("How many digits is the code? "))
print("TYPE OR CLICK DO NOT WORK ON THIS EXAMPLE, CLICK REQUIRES IMAGEs.")
entry_method = input("Type or click or Test? ")
max_value = int("9" * digits)

#pos = [pag.locateCenterOnScreen('0.jpg'), pag.locateCenterOnScreen('1.jpg'), pag.locateCenterOnScreen('2.jpg'), pag.locateCenterOnScreen('3.jpg'), pag.locateCenterOnScreen('4.jpg'), pag.locateCenterOnScreen('5.jpg'), pag.locateCenterOnScreen('6.jpg'), pag.locateCenterOnScreen('7.jpg'), pag.locateCenterOnScreen('8.jpg'), pag.locateCenterOnScreen('9.jpg')]
enterneeded = True
#ex, ey = pag.locateCenterOnScreen('enter.jpg')
time.sleep(5)
typing_speed = 0.0001


if entry_method == "Type":
    for i in range(max_value + 1):  # Include the maximum value in the range
        if kbrd.is_pressed('q'):
            break
        code = str(i).zfill(digits)
        
        for digit in code:
            if kbrd.is_pressed('q'):
                break
            kbrd.press(digit)
            time.sleep(typing_speed)
            kbrd.release(digit)
        kbrd.press_and_release('enter')

if entry_method == "Click":
    combinations = list(itertools.permutations(pos))
    for combo in combinations:
        if kbrd.is_pressed('q'):
            break
        for position in combo:
            if kbrd.is_pressed('q'):
                break
            x, y = position
            pag.click(x, y)
        if enterneeded == True:
            pag.click(ex, ey)

if entry_method == "Test":
    start_time = time.time()  # Start the timer
    
    for i in range(max_value + 1):  # Include the maximum value in the range
        if kbrd.is_pressed('q'):
            break
        code = str(i).zfill(digits)
        
        if int(code) == passw:
            end_time = time.time()  # Stop the timer
            elapsed_time = end_time - start_time  # Calculate time taken
            print("Password found:", code)
            print("Time taken:", elapsed_time, "seconds")
            break