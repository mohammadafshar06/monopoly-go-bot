import pygetwindow as gw
import time

# Window name for MEmu
window_title = "MEmu"  # Customize if the title is different

# Desired window size (do not change, otherwise the image recognition and clicking will not work properly)
new_width = 603 
new_height = 1031  

def resize_and_center():
    # Search the MEmu window
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        print(f"No window with the title'{window_title}' found.")
        return

    # Take the first window found (if there are several)
    window = windows[0]

    # Bring the window to the foreground    
    window.activate()
    time.sleep(1) 

    window.resizeTo(new_width, new_height)
    print(f"Fenstergröße auf {new_width}x{new_height} geändert.")

    window.moveTo(0, 0)


