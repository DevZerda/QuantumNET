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

        LogTypes.LogCommand(logResp)
        if logType == "attack":
            LogTypes.LogAttack(logResp)


class LogTypes:
    def LogCommand(logThis):
        logsDB = open("../db/logs.db", "a")
        logsDB.write(logThis)
        logsDB.close()

    def LogAttack(logThis):
        attkDB = open("../db/attacks.db", "a")
        attkDB.write(logThis)
        attkDB.close()

    def LogLogin(logThis):
        LoginDB = open("../db/logins.db", "a")
        LoginDB.write(logThis)
        LoginDB.close()


    