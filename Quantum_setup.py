import os, sys, time, platform

UnixPlatform = False

def GetOS():
    if "Windows" in platform.platform():
        UnixPlatform = False
    elif "Linux" in platform.platform():
        UnixPlatform = True
    elif "Darwin" in platform.platform():
        UnixPlatform = True
    else:
        print("[x] Error, This net does not support this OS")
        exit()
    

def WindowsInstall():
    os.system("pip install requests")
    os.system("pip install discord_webhook")

def UnixInstall():
    os.system("apt install python3-pip")
    os.system("pip3 install requests")
    os.system("pip3 install discord_webhook")

def CheckForPython3():
    if os.path.isfile("/usr/bin/python3"):
        print("Python3 is installed. In-order to run Quantum NET you'll have to use python3!")
