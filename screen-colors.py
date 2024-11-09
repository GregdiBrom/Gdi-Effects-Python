import win32gui
import win32api
import win32con
import random
import ctypes
import time

# Imposta il processo per essere DPI aware
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

# Ottieni le dimensioni dello schermo
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

# Memorizza il tempo di inizio
start_time = time.time()

# Loop per 2 secondi
while time.time() - start_time < 2:
    hdc = win32gui.GetDC(0)
    color = (random.randint(0, 122), random.randint(0, 430), random.randint(0, 310))
    brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
    win32gui.SelectObject(hdc, brush)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.SRCCOPY)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)
    # Libera le risorse del pennello
    win32gui.DeleteObject(brush)
    # Rilascia il contesto di dispositivo
    win32gui.ReleaseDC(0, hdc)
