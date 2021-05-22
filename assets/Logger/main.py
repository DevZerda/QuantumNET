## Modules
import os, sys, time

## Files
from ..Config.main import *
from ..Config.current import *
from ..utils.main import *

class MainLogger:
    def Log(logType):
        logResp = "Log: " + logType + " | Time: " + utils.CurrentTime() + "\n"
        logResp += "User: " + Current.CurrentInfo['Username'] + " | IP: " + Current.CurrentInfo['IP'] + "\n"
        logResp += "Level: " + Current.CurrentInfo['Level'] + " | Admin: " + Current.CurrentCmd['Admin'] + "\n"
        logResp += "Cmd: " + Current.CurrentCmd['Cmd'] + " | Full CMD: " + Current.CurrentCmd['Fullcmd'] + "\n"
        print(logResp)

    def LogCommand(logThis):
        logsDB = open("../db/users.db", "a")
        logsDB.write(logThis)
        logsDB.close()

    def LogAttack():
        return ""

    def LogLogin():
        return ""

    