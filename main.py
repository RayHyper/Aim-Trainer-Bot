import pyautogui
import win32api
import win32con
import PySimpleGUI as sg


sg.theme('LightBlue6')
sg.set_options(font=('Futura', 20))
layout = [[sg.Text("Aim Trainer Bot V1")],[sg.Text("https://aimtrainer.io/challenge")],[sg.Button("Start")]]
window = sg.Window("Bot",layout,element_justification="c",size=(500,200))
event, values = window.read()
window.close()


play = pyautogui.locateCenterOnScreen("play.PNG", confidence=0.65, grayscale=True)
if play:
    pyautogui.moveTo(play)
    pyautogui.leftClick()

else:
    sg.theme("LightBlue")
    sg.popup_ok("Error", "Aim Trainer Not Found", title="Error")
    exit(1)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while True:

    #disk = pyautogui.locateCenterOnScreen("realaim.PNG", confidence=0.90, grayscale=True,region = (561,361,1358,976))
    disk = pyautogui.locateCenterOnScreen("aim.PNG", confidence=0.65, grayscale=True)

    if disk:
        click(disk[0], disk[1])



