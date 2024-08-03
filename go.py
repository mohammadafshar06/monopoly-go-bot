import pyautogui
import time
from global_functions import click_at_position



def find_image_on_screen():
    try:
        location = pyautogui.locateOnScreen(r'assets\GO.png', region= (220, 780, 130, 100),grayscale=False, confidence=0.8)
        
        if location is not None:
            print(f"Picture found! Position: {location}")
            return True
        else:
            print("Image not found.")
            return False
    except Exception as e:
        print(f"An error has occurred: {e}")
        return False

def press_go_if_located():
    found = find_image_on_screen()
    if found:
        print("Dice...")
        click_at_position(280,837)
        time.sleep(2)





