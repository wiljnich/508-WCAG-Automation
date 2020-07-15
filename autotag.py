#x, y = pyautogui.position()
#print(x, y)

import warnings
import time
import glob
import pandas as pd
import pywinauto
import pyautogui
from pywinauto.application import Application

warnings.filterwarnings("ignore")
at = pd.read_csv('data/autotag.csv')['pdfs'].to_list()

def main():
    for x in glob.glob('pdfs/finished/*'):
        if str(x.split("\\")[1]) in at:
            time.sleep(10)
            app = Application().start('%s %s' % ("C:\Program Files (x86)\Adobe\Acrobat DC\Acrobat\Acrobat.exe",str(x)))
            time.sleep(5)
            pywinauto.mouse.click(button='left', coords=(1754, 835))
            time.sleep(3)
            pywinauto.mouse.click(button='left', coords=(1702, 272))
            time.sleep(20)
            pywinauto.mouse.click(button='left', coords=(30, 122))
            time.sleep(5)
            pywinauto.mouse.click(button='left', coords=(1885, 11))

if __name__ == "__main__":
    main()