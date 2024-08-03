import pyautogui
import time
from global_functions import click_at_position


def is_currently_on_fight():
    try:
        location = pyautogui.locateOnScreen(r'assets\switch_opponent.png', region= (138, 975, 286, 40),grayscale=True, confidence=0.8)
        
        if location is not None:
            print(f"Switch Opponent Button found! Position: {location}")
            return True
        else:
            print("Switch Opponent Button not found.")
            return False
    except Exception as e:
        print(f"An error has occurred: {e}")
        return False

def find_and_destroy_building():
    try:
        location = pyautogui.locateOnScreen(r'assets\find_building.png', region= (15, 220, 530, 680),grayscale=True, confidence=0.6)
        
        if location is not None:
            center_x = location.left + location.width // 2
            center_y = location.top + location.height // 2
            click_at_position(center_x, center_y)
                
            print(f"Building found! Position:{location}")
            return True
        else:
            print("Building not found.")
            return False
    except Exception as e:
        print(f"An error has occurred: {e}")
        return False


def is_collect_button_located():
    try:
        location = pyautogui.locateOnScreen(r'assets\collect_in_fight.png', region= (172, 943, 220, 50),grayscale=True, confidence=0.8)
        
        if location is not None:
            print(f"Collect Button found! Position: {location}")
            return True
        else:
            print("Collect button not found.")
            return False
    except Exception as e:
        print(f"An error has occurred:{e}")
        return False


def destroy_building():
    is_fight = is_currently_on_fight()
    if is_fight == True:
        for _ in range(30):
            is_destroyed = find_and_destroy_building()
            
            if is_destroyed == True:
                print("Building destroyed")
                while True:
                    if is_collect_button_located() == True:
                        click_at_position(275, 969)
                        break
                    time.sleep(0.5)
                return
            time.sleep(0.09)  

