import os, sys, time
from .crud import *

class CrudFunctions:
    def TokenValidation(rtoken):
        return ""
        
    def ChangePW(user, newpw):
        info = CRUD.GetUser(user).split(",")
        CRUD.RemoveUser(user)
        CRUD.CreateUser(info[0], newpw, info[3], info[4], info[5])


    def IPChange(user, newip):
        return ""

    def isRegistered(username):
        info = CRUD.GetUser(username)
        if info == "[x] Error, No user found!":
            return False

        return True
    
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

    def isReseller(username):
        info = CRUD.GetUser(username)
        if info == "[x] Error, No user found!":
            return "[x] Error, No user found!\r\n (This seems like a buggy function)"

        info = info.split(",")
        if int(info[5]) == 1:
            return True
        else:
            return False

    def isAdmin(username):
        info = CRUD.GetUser(username)
        if info == "[x] Error, No user found!":
            return "[x] Error, No user found!\r\n (This seems like a buggy function)"

        info = info.split(",")
        if int(info[5]) == 2:
            return True
        else:
            return False

    def isOwner(username):
        info = CRUD.GetUser(username)
        if info == "[x] Error, No user found!":
            return "[x] Error, No user found!\r\n (This seems like a buggy function)"

        info = info.split(",")
        if int(info[5]) == 3:
            return True
        else:
            return False
