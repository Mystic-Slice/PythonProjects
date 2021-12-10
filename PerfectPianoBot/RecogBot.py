from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api,win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(384,400)[0] == 0:
        click(384,400)
    if pyautogui.pixel(454,400)[0] == 0:
        click(454,400)
    if pyautogui.pixel(524,400)[0] == 0:
        click(524,400)
    if pyautogui.pixel(594,400)[0] == 0:
        click(594,400)    

#Piano tiles position
#1: 384
#2: 454
#3: 524
#4: 594
