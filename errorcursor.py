import ctypes
import time
import win32con


LoadIcon = ctypes.windll.user32.LoadIconW
GetCursorPos = ctypes.windll.user32.GetCursorPos
DrawIcon = ctypes.windll.user32.DrawIcon
GetDC = ctypes.windll.user32.GetDC
ReleaseDC = ctypes.windll.user32.ReleaseDC

hIcon = LoadIcon(0, win32con.IDI_ERROR)


class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


max_execution_time = 4

try:
    start_time = time.time()  
    while time.time() - start_time < max_execution_time:
        # Ottieni la posizione corrente del cursore
        pt = POINT()
        GetCursorPos(ctypes.byref(pt))


        hdc = GetDC(0)


        DrawIcon(hdc, pt.x, pt.y, hIcon)

        # Rilascia il device context
        ReleaseDC(0, hdc)

    
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Programma terminato.")

