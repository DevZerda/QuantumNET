# Modules
import os
import sys
import time

# Files
from assets.utils.main import *


def Check4Modules():
    return ""


def InstallModules():
    # steven -> i have no idea what the function does
    if utils.GetOS() == True:
        pipCheck = subprocess.getoutput("pip3 --version")
        py3Check = subprocess.getoutput("python3 --version")
        if "command not found" in pipCheck:
            # install pip
            os.system('apt install python3 -y > /dev/null')
        if "command not found" in py3Check:
            # install py3
            os.system('apt install python3-pip -y > /dev/null')
