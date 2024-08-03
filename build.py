import pyautogui
import os
import time
from global_functions import click_at_position

image_files = [r"assets\images_build\build_1.png",
                r"assets\images_build\build_2.png",
                r"assets\images_build\build_3.png",
                r"assets\images_build\build_4.png",
                r"assets\images_build\build_5.png"]

copy_image_files = [r"assets\images_build\build_1.png",
                r"assets\images_build\build_2.png",
                r"assets\images_build\build_3.png",
                r"assets\images_build\build_4.png",
                r"assets\images_build\build_5.png"]


found_at = ""

def find_buildimages_in_region():
    try:
        if not image_files:
            print("No image files found in the specified folder.")
            return False

        for image_file in image_files:
            image_path = os.path.join(image_file)
            print(f"Search for {image_file}...")
            location = pyautogui.locateOnScreen(image_path, region=(83,910, 100, 110), grayscale=True, confidence=0.95)

            if location is not None:
                global found_at
                found_at = image_file
                print(f"{image_file} found in position: {location}")
                return True
            
        print("None of the pictures were found.")
        return False

    except Exception as e:
        print(f"An error has occurred: {e}")
        return False


def find_buildings_and_click():
    try:
        # Suche das Bild auf dem Bildschirm
        location = pyautogui.locateOnScreen(r"assets\images_build\find_buildings.jpg", region= (15, 760, 540, 25),grayscale=True, confidence=0.8)
        
        # Überprüfe, ob das Bild gefunden wurde
        if location is not None:
            print(f"Bild gefunden! Position: {location}")
            # Berechne die Mitte des gefundenen Bereichs
            center_x = location.left + location.width // 2
            center_y = location.top + location.height // 2
            click_at_position(center_x, center_y)
            
            return True
        else:
            print("Bild nicht gefunden.")
            return False
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return False

def is_clicked():
    try:
        # Suche das Bild auf dem Bildschirm
        location = pyautogui.locateOnScreen(r"assets\images_build\no_buildings.jpg", region= (457, 340, 35, 30),grayscale=True, confidence=0.8)
        
        # Überprüfe, ob das Bild gefunden wurde
        if location is not None:
            print(f"Bild gefunden! Position: {location}")
            return True
        else:
            print("Bild nicht gefunden.")
            return False
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return False

def upgrade_building():
    global image_files
    found = find_buildimages_in_region()
    if found == True:
        click_at_position(130, 970)
        time.sleep(2)
        clicked = find_buildings_and_click()
        time.sleep(2)
        if clicked == True:
            not_build = is_clicked()
            if not_build == True:
                if found_at in image_files:
                    image_files.remove(found_at)
                click_at_position(472, 355)
                click_at_position(283, 1000)
            else :
                image_files = copy_image_files
                click_at_position(283, 1000)
                time.sleep(3)

