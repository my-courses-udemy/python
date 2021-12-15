import pyautogui, webbrowser
from time import sleep

def open_browser(date, wait_first, wait_second):
    webbrowser.open_new(f'https://www.messenger.com/t/100065990881770')
    sleep(wait_first)
    
    pyautogui.typewrite(date) 
    sleep(wait_second)
    pyautogui.press("enter")
    pyautogui.hotkey("ctrl", "w")