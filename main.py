import pyautogui
import win32api
import win32con
from pymsgbox import alert


alert(text='Aim Trainer Bot', title='Aimbot', button='Confirm')

play = pyautogui.locateCenterOnScreen("play.PNG", confidence=0.65, grayscale=True)
pyautogui.moveTo(play)
pyautogui.leftClick()


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while True:
    #disk = pyautogui.locateCenterOnScreen("realaim.PNG", confidence=0.90, grayscale=True,region = (561,361,1358,976))
    disk = pyautogui.locateCenterOnScreen("aim.PNG", confidence=0.60, grayscale=True)
    if disk:
        click(disk[0], disk[1])
