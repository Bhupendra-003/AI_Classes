import pyautogui
import time

# Delay to give you time to switch to the window you want to test
time.sleep(3)

# Move the cursor in a square pattern
while(True):  # repeat 3 times
    pyautogui.moveRel(100, 0, duration=0.5)   # right
    pyautogui.moveRel(0, 100, duration=0.5)   # down
    pyautogui.moveRel(-100, 0, duration=0.5)  # left
    pyautogui.moveRel(0, -100, duration=0.5)  # up
