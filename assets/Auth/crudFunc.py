import os, sys, time
from .crud import *

class CrudFunctions():
    def isRegistered(username):
        info = CRUD.GetUser(username)
    
    def isPremium(username):
        info = CRUD.GetUser(username)
        if info == "[x] Error, No user found!":
            return "[x] Error, No user found!\r\n (This seems like a buggy function)"

        info = info.split(",")
        if int(info[3]) == 0:
            return False
        elif int(info[3]) > 0 & int(info[3]) <= 5:
            return True
        else:
            return False