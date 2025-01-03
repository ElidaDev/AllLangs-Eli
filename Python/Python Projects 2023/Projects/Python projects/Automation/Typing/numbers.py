import keyboard as pag
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
print("Numbers from Min To max")
a = int(input("Every: "))
min_val = int(input("Minimum: "))
max_val = int(input("Maximum: "))
wait = float(input("Wait: "))
do_typing = True
mc = True #True opens the chat in minecraft, by pressing 't' prior to sending the message.
time.sleep(5)

for num in range(min_val, max_val + 1, a):
    if do_typing:
        if pag.is_pressed('q'):
            break
        pag.write(str(num))
        pag.press_and_release('enter')
        if mc == True:
            pag.press_and_release('t')
        time.sleep(wait)
    else:
        if pag.is_pressed('q'):
            break
        print(num)
        time.sleep(wait)