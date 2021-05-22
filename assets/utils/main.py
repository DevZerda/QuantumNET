from Quantum_setup import GetOS
import os, sys, time, platform

class utils:
    def set_Title(socket, msg):
        return "\033]0;" + msg + "\007"

    def set_Cursor(socket, r, c):
        return ""
    
    def moveLeft_Cursor(socket):
        return ""

    def moveRight_Cursor(socket):
        return ""
    
    def moveUp_Cursor(socket):
        return

    def moveDown_Cursor(socket):
        return

    def removeRow(socket):
        return ""

    def CurrentTime():
        return ""

    def CheckForPython3Unix():
        if GetOS() == True:
            if os.path.isfile("/usr/bin/python3"):
                return True
            else:
                return False

    def GetOS():
        print(platform.platform())
        if "Windows" in platform.platform():
            return False
        elif "Linux" in platform.platform():
            return True
        else:
            print("[x] Error, This net does not support this OS")
            exit()