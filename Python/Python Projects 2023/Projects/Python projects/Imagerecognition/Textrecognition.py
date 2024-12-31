import time
import pyautogui

# Function to move the mouse to a specific position
def move_mouse(x, y):
    pyautogui.moveTo(x, y, duration=0.25)

# Function to click the mouse
def click_mouse():
    pyautogui.click()

# Function to check for the fishing bobber splash sound
def is_splash_sound():
    # Check for the color of the water around the bobber
    water_color = pyautogui.pixel(500, 500)  # Replace these coordinates with the actual location of your bobber
    return water_color == (83, 119, 255)  # Adjust the color based on your Minecraft settings

# Function to automate fishing in Minecraft
def automate_fishing():
    print("Starting automated fishing...")

    # Move to the water source (replace these coordinates with your screen resolution)
    move_mouse(500, 500)
    time.sleep(2)

    # Cast the fishing rod
    click_mouse()
    time.sleep(2)

    # Monitor for the fishing bobber splash sound
    while True:
        if is_splash_sound():
            print("Fish caught! Reeling in...")
            click_mouse()
            time.sleep(2)
            # Cast the rod again
            click_mouse()
            time.sleep(2)

# Main function
def main():
    # Wait for the user to focus on Minecraft
    input("Please focus on Minecraft and press Enter...")

    # Automate fishing
    automate_fishing()

    print("Task completed. Exiting...")

if __name__ == "__main__":
    main()
