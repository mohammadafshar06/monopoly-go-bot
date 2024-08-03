import time
import threading

from resize_screen import resize_and_center
from go import press_go_if_located
from jail import press_jail_if_located
from build import upgrade_building
from bank_heist import bank_heist
from fight import destroy_building
from tutorial import press_finger_if_located, collect_from_building_level_up, exit_building__check_if_stuck, go_next_lev


def thread_function():
    while True:
        for _ in range(4):
            press_finger_if_located()
            time.sleep(0.7)
        collect_from_building_level_up()
        exit_building__check_if_stuck()
        go_next_lev()
        time.sleep(30)




thread = threading.Thread(target=thread_function)
thread.start()
resize_and_center() 

time.sleep(3)

while True:
    press_go_if_located()
    time.sleep(1)
    
    press_jail_if_located()
    bank_heist()
    destroy_building()
    
    upgrade_building()