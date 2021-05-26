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

    def changeMOTD(new_motd):
        motd = open("./assets/db/motd.db", "w")
        motd.write(new_motd)
        motd.close()
        return f"MOTD Successfully changed to ({new_motd})"

    def GetMOTD():
        motd = open("./assets/db/motd.db", "r").read()
        return motd


class OS_Func:
    def GetOSType():
        if "Windows" in platform.platform():
            return False
        elif "Linux" in platform.platform():
            return True
        else:
            print("[x] Error, This net does not support this OS")
            exit()

class arrUtils:
    def arr2str(arr):
        if isinstance(arr, list) == False:
            print("[x] Error, Invalid value provided!")
            exit(0)
        n_str = ""
        for u in arr:
            n_str += u

        return n_str


