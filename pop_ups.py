import pyautogui
from global_functions import click_at_position



def find_image_on_screen(image_path, region):
    try:
        location = pyautogui.locateOnScreen(image_path, region= region,grayscale=True, confidence=0.8)
        
        if location is not None:
            print(f"Picture found! Position:{location}")
            return True
        else:
            print("Image not found.")
            return False
    except Exception as e:
        print(f"An error has occurred:{e}")
        return False
    
def decline_feedback():
    find_image_on_screen("assets\decline_feedback.png", (142, 707, 290, 65))
    click_at_position(280,736)
    click_at_position(280,825)

decline_feedback()