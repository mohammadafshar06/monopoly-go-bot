import pyautogui
import time
from global_functions import click_at_position


image_to_find = r'assets\jail_roll.png'  

def find_image_on_screen(image_path):
    try:
        location = pyautogui.locateOnScreen(image_path, region= (205, 803, 150, 60),grayscale=True, confidence=0.8)
        
        if location is not None:
            print(f"Picture found! Position: {location}")
            return True
        else:
            print("Image not found.")
            return False
    except Exception as e:
        print(f"An error has occurred: {e}")
        return False

def press_jail_if_located():
    while True: 
        found = find_image_on_screen(image_to_find)
        if found:
            print("Break out...")
            click_at_position(280,837)
            time.sleep(2.3)
        else: break





