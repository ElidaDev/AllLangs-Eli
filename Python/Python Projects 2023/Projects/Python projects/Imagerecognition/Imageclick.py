import pyautogui
from PIL import ImageGrab

# Capture the entire screen as an image
pil_img = ImageGrab.grab()

# Attempt to locate the image on the captured screenshot
location = pyautogui.locateCenterOnScreen("Clickthis.png", confidence=0.75)

if location is not None:
    x, y = location
    # Move the mouse cursor to the located coordinates slowly
    pyautogui.moveTo(x, y, duration=2)  # Adjust the duration as needed
    # Click at the located coordinates (optional)
    pyautogui.click(x, y)
    print(f"Moved to ({x}, {y}) and clicked.")
else:
    print("Image not found on the screen")