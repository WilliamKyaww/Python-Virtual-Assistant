import win32com.client

def find_airpods(name):
    # Shell object
    shell = win32com.client.Dispatch("WScript.Shell")

    # Windows key + R
    shell.SendKeys("^R")
    shell.SendKeys("ms-settings:bluetooth")

find_airpods("William's AirPods")
ms-settings:bluetooth