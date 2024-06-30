'''
@author Josh Gilstrap

A script that resets the drivers of my MSI Raider GE78HX 13VG touchpad.

The problem:
My touchpad freezes periodically during normal useage. Takes several seconds
and many inputs to unfreeze.

The solution:
Automatically fire this script using Task Scheduler whenever the mouse freezes.
'''

import subprocess
import time
import logging
from pynput.mouse import Listener

logging.basicConfig(filename='mouse_monitor.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

DEVCON_PATH = r"C:\Program Files (x86)\Windows Kits\10\Tools\10.0.26100.0\x64\devcon.exe"

mouse_active = True

def restart_mouse_driver():
    try:
        logging.info("Attempting to restart mouse driver.")
        # Stop the mouse driver
        subprocess.run([DEVCON_PATH, "disable", r"HID\ELAN0305&COL03\5&39B7652F&0&0002"], check=True)
        time.sleep(1) 
        # Start the mouse driver
        subprocess.run([DEVCON_PATH, "enable", r"HID\ELAN0305&COL03\5&39B7652F&0&0002"], check=True)
        logging.info("Mouse driver restarted successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to restart mouse driver: {e}")

def on_move(x, y):
    global mouse_active
    mouse_active = True

def on_click(x, y, button, pressed):
    global mouse_active
    mouse_active = True

def on_scroll(x, y, dx, dy):
    global mouse_active
    mouse_active = True

def monitor_mouse():
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()

def main():
    restart_mouse_driver()

if __name__ == "__main__":
    logging.info("Starting mouse monitor script.")
    while True:
        mouse_active = False
        monitor_mouse()
        time.sleep(5)
        if not mouse_active:
            logging.warning("Mouse inactive. Restarting driver...")
            restart_mouse_driver()