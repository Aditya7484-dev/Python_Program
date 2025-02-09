import pyautogui
import time
import pyperclip

pyautogui.click(318,1049)
time.sleep(3)

pyautogui.moveTo(162,285)
pyautogui.dragTo(982,1010,duration=1.0,button='left')

pyautogui.hotkey('ctrl','c')
time.sleep(1)

text=pyperclip.paste()

print(text)