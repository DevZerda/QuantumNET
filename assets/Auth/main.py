## Modules
import os, sys, time

## Files
from .crud import *
from .crudFunc import *

class Auth():
    def Login(user, pw, ip):
        get_info = CRUD.GetUser(user)
        if "[x]" in get_info:
            return "[x] Error, Incorrect username or password. Try again...."

        info = get_info.split(",")

        if info[0] == user and info[2] == pw:
            if info[1] == "none":
                CrudFunctions.IPChange(user, ip)
            ## Log This Login
            return f"[+] Successfully logged in, Welcome: {user}"
        else:
            return f"[x] Error, Incorrect username or password. Try again...."