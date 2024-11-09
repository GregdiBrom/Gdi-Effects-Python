from win32gui import *
from win32ui import *
from win32api import *
import time

hwnd = GetDesktopWindow()
hdc2 = GetWindowDC(hwnd)
x2 = GetSystemMetrics(0)
y2 = GetSystemMetrics(1)

def tunnel_effect():
    start_time = time.time()
    while time.time() - start_time < 3:  
        StretchBlt(hdc2, 25, 25, x2 - 50, y2 - 50, hdc2, 0, 0, x2, y2, 0x00CC0020)
        time.sleep(0.04) 

tunnel_effect()
