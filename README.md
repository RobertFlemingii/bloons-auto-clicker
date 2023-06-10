Keyboard Spamming Tool
This is a Python script that allows you to spam keystrokes on your keyboard. It utilizes the pynput library to control the keyboard inputs and the keyboard library to detect key presses. The script is designed to spam a sequence of numbers (1-9) when a specific key is pressed.

Prerequisites
Before running the script, make sure you have the following prerequisites installed:

Python 3.x
pynput library
keyboard library
win32gui library
win32api library
win32con library

You can install the required libraries using pip:
pip install pynput keyboard pywin32

Usage
Import the necessary libraries:

from pynput.keyboard import Controller
import time
import keyboard
import win32gui
import win32api
import win32con

Create an instance of the Controller class from pynput.keyboard:

myKeyboard = Controller()
Run an infinite loop to continuously check for key presses:

    while True:

Inside the loop, check if the specified key (in this case, 'q') is pressed using the keyboard.is_pressed() function:

    if keyboard.is_pressed('q'):

If the key is pressed, start spamming the numbers 1-9:

        print('Powering up')
        i = 0
        while i != 10:
            if not i == 20:
                time.sleep(.1)
                keyboard.press(str(i))
                keyboard.release(str(i))
            if not (i ^ 9):
                i = 0
            else:
                i = i + 1
            if keyboard.is_pressed('p'):
                print('Powering down')
                i = 10

Stop the script by pressing the 'p' key.

Note
There is a commented out section of code that is meant for handling window focus. This code is currently disabled in the script. If you want to enable it and customize it to your needs, you can uncomment the relevant code block and modify it accordingly.

That's it! You can now run the script and spam keystrokes when the 'q' key is pressed. Make sure to review and modify the script according to your requirements before running it.

Disclaimer: Be mindful when using this script and ensure that you have appropriate permissions to interact with applications or systems. Misuse of this script may violate terms of service or applicable laws. Use it responsibly.
