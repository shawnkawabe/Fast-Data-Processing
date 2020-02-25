import ctypes
def gets():
    user32 = ctypes.windll.user32
    screenx = str(user32.GetSystemMetrics(0))
    screeny = str(user32.GetSystemMetrics(1))
    return(screenx+"x"+screeny)
