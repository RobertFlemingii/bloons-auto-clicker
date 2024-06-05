Bloons Auto Clicker
Overview
Bloons Auto Clicker is a Python script designed to automate the activation of Special Abilities in the game Bloons TD 6. This script allows you to spam a sequence of numbers (1-9) when a specific key is pressed, enhancing your gameplay by automating the activation of abilities.

Prerequisites
Before running the script, ensure you have the following installed:

Python 3.x
pynput library
keyboard library
pywin32 package (includes win32gui, win32api, win32con)
You can install the required libraries using pip:

bash
Copy code
pip install pynput keyboard pywin32
How to Use
Download the Script:

Save the bloons-auto-clicker.py file to your local machine.

Run the Script:

Open a terminal or command prompt, navigate to the directory containing the script, and run:

bash
Copy code
python bloons-auto-clicker.py
In-Game Usage:

Start Spamming Abilities:

Press the q key to start spamming the numbers 1-9, which will activate the corresponding Special Abilities in Bloons TD 6.
You should see a message "Powering up" indicating the script is active.
Stop Spamming Abilities:

Press the p key to stop the spamming.
You should see a message "Powering down" indicating the script has stopped.
Note
There is a commented-out section of code intended for handling window focus. This code is currently disabled in the script. If you want to enable it and customize it to your needs, you can uncomment the relevant code block and modify it accordingly.
