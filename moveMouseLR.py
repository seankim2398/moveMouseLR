### The program automatically moves the mouse left and right with the shift key used as play/pause and the esc key used to quit the program

import pyautogui
from pynput.keyboard import Key, Listener

# Get screen size
width, height = pyautogui.size()

is_running = False
first_run = True
exit = False

# When shift/esc is pressed it will notify the Listener
def on_press(key):
    global is_running
    global exit

    # toggle key to start/pause movement of mouse
    if key == Key.shift:
        is_running = not is_running
        if is_running:
            print("Moving")
        else:
            print("Pausing")
    # esc key to exit program
    elif key == Key.esc:
        is_running = False
        print("Quitting")
        exit = True

with Listener(on_press=on_press) as listener:
    while not exit: 
        # if shift is pressed, then the program is running
        if is_running:
            # is_running is on every if statement because the user at anytime can pause the program without having to wait for 4 different mouse movements
            # checks if it is the first_run whether that is from cold start or after the program was paused
            # initializes screen for movement left and right
            if is_running and first_run:
                pyautogui.moveTo(width/2, height/2, duration=0.5)  # Move mouse to center of screen
                pyautogui.move(width/2, 0, duration=1.5) # Move to the right side of screen
                first_run = False 

            if is_running:
                pyautogui.move(-width, 0, duration=2) # Move left of the whole screen 
            if is_running:
                pyautogui.move(width, 0, duration=2) # Move right of the whole screen 
        # program is paused
        else:
            first_run = True
            pass
