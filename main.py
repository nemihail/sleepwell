
import tkinter.messagebox
from time import sleep
import pygetwindow
import datetime

# made by ne dynamics, tg: @shulepok

while True:
    try:
        hours = datetime.datetime.now().hour
        need_to_close = pygetwindow.getWindowsWithTitle('FireFox')
        if hours >= 23:
            if need_to_close:
                need_to_close = need_to_close[0]
                need_to_close.close()
                tkinter.messagebox.showwarning('sleepwell', 'youre gonna sleep, not youtube!')
        sleep(1)
    except KeyboardInterrupt:
        pass
