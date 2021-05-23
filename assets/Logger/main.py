## Modules
import os, sys, time

## Files
from ..Config.main import *
from ..Config.current import *
from ..utils.main import *
from .discord import *

class MainLogger:
    def Log(logType, notification):
        logResp = "Log: " + logType + " | Time: " + str(utils.CurrentTime()) + "\n"
        if "CMD" in logType:
            logResp += "User: " + Current.CurrentInfo['Username'] + " | IP: " + Current.CurrentInfo['IP'] + "\n"
            logResp += "Level: " + str(Current.CurrentInfo['Level']) + " | Admin: " + str(Current.CurrentInfo['Admin']) + "\n"
            logResp += "Cmd: " + Current.CurrentCmd['Cmd'] + " | Full CMD: " + Current.CurrentCmd['fullcmd'] + "\n"
        print(logResp)

        LogTypes.LogCommand(logResp)
        if logType == "attack":
            LogTypes.LogAttack(logResp)
        elif logType == "login":
            LogTypes.LogLogin(logResp)
        elif logType == "status":
            LogTypes.Log

        Discord.send_logs(logResp)



class LogTypes:

    def sendDiscord(Type, msg):
        if Type == "attack":
            Discord.send_attack(msg)
        elif Type == "status":
            Discord.send_status(msg)
        elif Type == "login":
            Discord.send_login(msg)

    def LogCommand(logThis):
        logsDB = open(os.getcwd() + "/assets/db/logs.db", "a")
        logsDB.write(logThis)
        logsDB.close()

    def LogAttack(logThis):
        attkDB = open("./db/attacks.db", "a")
        attkDB.write(logThis)
        attkDB.close()
        

    def LogLogin(logThis):
        LoginDB = open("./db/logins.db", "a")
        LoginDB.write(logThis)
        LoginDB.close()


    