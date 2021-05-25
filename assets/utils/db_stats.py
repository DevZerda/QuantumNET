import os, sys, time

class db_Stats:
    def TotalUsers():
        db = len((open("./assets/db/users.db", "r").read()).split("\n"))
        return db

    def OnlineUsers():
        db = len((open("./assets/db/current.db", "r").read()).split("\n"))
        return db

    def TotalAttack():
        db = len((open("./assets/db/attacks.db", "r").read()).split("\n"))