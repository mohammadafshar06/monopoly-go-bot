import pyautogui
import os
import time
from global_functions import click_at_position


def find_buildings_and_click(click = True):
    try:
        location = pyautogui.locateOnScreen(r"assets\bank_heist.png", region= (44, 512, 480, 468),grayscale=True, confidence=0.8)
        
        if location is not None:
            print(f"Picture found! Position: {location}")
            center_x = location.left + location.width // 2
            center_y = location.top + location.height // 2
            if click == True:
                click_at_position(center_x, center_y)
            
            return True
        else:
            print("Bank Heist: False")
            return False
    except Exception as e:
        print(f"An error has occurred: {e}")
        return False
    

def bank_heist():
    if find_buildings_and_click(click=False) == False:
        return
    for i in range(7):
        find_buildings_and_click()
        print("Stealed " + str(i+1) + " time/s")
    time.sleep(4)
    click_at_position(285,969)
