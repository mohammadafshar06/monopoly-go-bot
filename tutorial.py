import pyautogui
import time
from global_functions import click_at_position
import os



def press_finger_if_located():
    try:
        location = pyautogui.locateOnScreen(r'assets\tutorial_finger.png', region= (10, 50, 545, 970),grayscale=False, confidence=0.8)
        
        if location is not None:
            print("Shit..i hate these tutorials...")
            print(f"Tutorial finger found! Position: {location}")
            click_every_12_pixels(location)
            return True
        else:
            print("Tutorial finger not found.")
            return False
    except Exception as e:
        print(f"An error has occurred:{e}")
        return False

def click_every_12_pixels(location):
    start_x = location.left
    start_y = location.top
    end_x = location.left + location.width
    end_y = location.top + location.height

    # Iterate over all 12 pixels in the defined area    
    for x in range(start_x, end_x, 12):
        for y in range(start_y, end_y, 12):
            pyautogui.click(x, y)
            time.sleep(0.01)  # Wait 0.01 seconds between clicks



def collect_from_building_level_up():
    try:
        location = pyautogui.locateOnScreen(r'assets\collect_from_building_level_up.png', region= (174, 927, 220, 53),grayscale=True, confidence=0.8)
        
        if location is not None:
            print(f"Collect Button found! Position: {location}")
            click_at_position(280, 957)
            return True
        else:
            print("Collect Button not found.")
            return False
    except Exception as e:
        print(f"An error has occurred: {e}")
        return False


def exit_building__check_if_stuck():
    consecutive_finds = 0

    while consecutive_finds < 5:
        location = pyautogui.locateOnScreen(r'assets\images_build\exit_building_checking_if_stuck.png', region=(255, 980, 52, 39), grayscale=True, confidence=0.8)
        
        if location is not None:
            print(f"Stuck? Exit button found at position:{location}.")
            consecutive_finds += 1
        else:
            print("Stuck? Exit button not found.")
            break
        time.sleep(1)

    # When the image has been found continuously for 5 seconds, click on it    
    if consecutive_finds == 5:
        click_at_position(280,1000)

def go_next_lev():
    try:
        location = pyautogui.locateOnScreen(r'assets\next_level_go.png', region= (230, 930, 107, 50),grayscale=True, confidence=0.8)
        
        if location is not None:
            print(f"Collect Button found! Position: {location}")
            click_at_position(275, 950)
            return True
        else:
            print("Collect Button not found.")
            return False
    except Exception as e:
        print(f"An error has occurred: {e}")
        return False




image_files = [
    r"assets\images_wins\wins_1.png",
    r"assets\images_wins\wins_2.png",
    	        ]

def is_quest_fullfilled():
    try:
        # Check whether the folder contains images       
        if not image_files:
            print("No image files found in the specified folder.")
            return False

        # Search every image in the folder        
        for image_file in image_files:
            image_path = os.path.join(image_file)
            print(f"Search for {image_file}...")
            location = pyautogui.locateOnScreen(image_path, region=(53,917, 40, 40), grayscale=True, confidence=0.9)

            if location is not None:
                global found_at
                found_at = image_file
                print(f"Quest completed: {location}")
                return True
            
        print("No quest completed.")
        return False

    except Exception as e:
        print(f"An error has occurred: {e}")
        return False

def search_and_click__tap_to_claim():
    try:
        location = pyautogui.locateOnScreen(r"assets\images_wins\tap_to_claim.png", region= (140, 360, 285, 600),grayscale=True, confidence=0.8)
        
        if location is not None:
            print(f"Claim Button found! Position: {location}")
            center_x = location.left + location.width // 2
            center_y = location.top + location.height // 2
            click_at_position(center_x, center_y)
            search_and_click__tap_to_claim()
            return
        else:
            print("Claim Button not found")
            return
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return
    

def collect_quest_rewards():
    if is_quest_fullfilled() == True:
        click_at_position(40,950)
        time.sleep(3)
        search_and_click__tap_to_claim()
        time.sleep(2)
        click_at_position(275,960)
        time.sleep(4.5)
        click_at_position(280,1000)

    

