import pyautogui
from pymsgbox import alert

import mouse

alert(text='Aim Trainer Bot', title='Aimbot', button='Confirm')

while True:
    disk = pyautogui.locateCenterOnScreen("aim.png", confidence = 0.70, grayscale = True)
    pyautogui.moveTo(disk)
    pyautogui.leftClick()








