from pynput.keyboard import Controller
import time
import keyboard
import datetime as dt
import win32gui
import win32api
import win32con

""" def callback(nCode, wParam, lParam):
    if wParam == win32con.WM_ACTIVATEAPP:
        hwnd = win32gui.GetForegroundWindow()
        class_name = win32gui.GetClassName(hwnd)
        window_title = win32gui.GetWindowText(hwnd)
        print(f"Clicked on window: {class_name} - {window_title}")
    return win32api.CallNextHookEx(hook, nCode, wParam, lParam)
hook = win32api.SetWindowsHookEx(win32con.WH_CALLWNDPROC, callback, 0, 0)
win32gui.PumpMessages()
win32api.UnhookWindowsHookEx(hook) """

myKeyboard = Controller()


while True:


    # start spamming at key press
    # print(win32gui.GetForegroundWindow())
    if keyboard.is_pressed('q'):
        print('Powering up')
        i = 0
        # press 1-9 and repeat
        while i != 10:
            # exceptions
            if not i == 20:
                time.sleep(.1)
                keyboard.press(str(i))
                keyboard.release(str(i))
            # reset or increment counter
            if not (i ^ 9):
                i = 0
            else:
                i = i + 1
            # stop spamming at key press
            if keyboard.is_pressed('p'):
                print('Powering down')
                i = 10
            # stop spamming at window focus; start again at refocus
"""             if active_hwnd != hwnd:
                # i = 10
                print('not focused')
                while True:
                    print(active_hwnd)
                    if active_hwnd == window_title:
                        # i = 0
                        print('focused')
                    time.sleep(2) """
            # 
