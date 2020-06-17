#import pyautogui, sys
#x, y = pyautogui.position()
#print(x, y)

import warnings
import time
import glob
import pywinauto
from pywinauto.application import Application

warnings.filterwarnings("ignore")

def main():
    for x in glob.glob('*.pdf'):
        time.sleep(10)
        app = Application().start('%s %s' % ("C:\Program Files (x86)\Adobe\Acrobat DC\Acrobat\Acrobat.exe",str(x)))
        time.sleep(5)
        pywinauto.mouse.click(button='left', coords=(211, 35))
        pywinauto.mouse.move(coords=(226, 75))
        pywinauto.mouse.click(button='left', coords=(434, 75))
        time.sleep(20)
        pywinauto.mouse.click(button='left', coords=(1857, 161))
        time.sleep(10)
        pywinauto.mouse.click(button='left', coords=(1670, 216))
        time.sleep(4)
        pywinauto.mouse.click(button='left', coords=(1683, 270))
        pywinauto.mouse.click(button='left', coords=(1715, 319))
        pywinauto.mouse.click(button='left', coords=(1873, 556))
        time.sleep(10)
        pywinauto.mouse.click(button='left', coords=(657, 758))
        time.sleep(4)
        pywinauto.mouse.click(button='left', coords=(980, 716))
        time.sleep(2)
        pywinauto.mouse.click(button='left', coords=(1018, 528))
        pywinauto.mouse.click(button='left', coords=(1888, 15))

if __name__ == "__main__":
    main()