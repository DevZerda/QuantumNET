import os, sys, time, subprocess

class PythonCheck:
    def LinuxPython3Check():
        check = subprocess.getoutput("python3")
        if "command not found" in check:
            return False
        else:
            return True

    def LinuxPip3Check():
        check = subprocess.getoutput("pip3")
        if "command not found" in check:
            return False
        else:
            return True

class PythonInstalls():
    def installPython3():
        os.system("sudo yum install python3")
        os.system("sudo apt install python3")
        os.system("sudo yum install pip3")
        os.system("sudo apt install pip3")

    def installDependencies():
        os.system("")