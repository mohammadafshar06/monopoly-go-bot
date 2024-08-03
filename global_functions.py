import pyautogui

def click_at_position(x, y):
    pyautogui.moveTo(x, y, duration=0.5)  
    pyautogui.click()  
    print(f"Clicked at position ({x}, {y})")