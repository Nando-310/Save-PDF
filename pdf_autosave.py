import pyautogui
from time import sleep


def take_screenshot():
    image = pyautogui.screenshot()
    image.save('screenshot.png')

screenshot_count = 0
max_screenshots = 5
while screenshot_count < max_screenshots:
    cp = pyautogui.locateOnScreen('cutepdf2.png', confidence=0.8)
    if cp is None:
        take_screenshot()
        sleep(5)
        screenshot_count += 1
    else:
        print(f"CutePDF found at {cp}")
        pyautogui.click(cp)
        sleep(4)
        sb = pyautogui.locateCenterOnScreen('savebutton.png',confidence=0.5)
        if sb is not None:
            print(f"Save button found at {sb}")
            pyautogui.click(sb)
        screenshot_count = 0
        sleep(2)







