from Quantum_setup import GetOS
import os, sys, time, platform, datetime

class utils:
    def set_Title(socket, msg):
        socket.send(f"\033]0;{msg}\007".encode())

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

    def removeAllToStart(socket):
        socket.send("\033[1K".encode())

    def CurrentTime(): # This is date and time not just time !
        return datetime.datetime.now()

    def CheckForPython3Unix():
        if GetOS() == True:
            if os.path.isfile("/usr/bin/python3"):
                return True
            else:
                return False

    def FlashingCursor(socket):
        while(True):
            socket.send("\033[?25l".encode())
            time.sleep(1)
            socket.send("\033[?25h\033[?0c".encode())
            time.sleep(1)

    def MOTD(motd):
        return ""


class OS_Func:
    def GetOSType():
        if "Windows" in platform.platform():
            return False
        elif "Linux" in platform.platform():
            return True
        else:
            print("[x] Error, This net does not support this OS")
            exit()

