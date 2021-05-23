## Modules
import os, sys, time

## Files
from ..Auth.crud import *
from ..utils.main import *

def Admin_Command(socket, argv):
    if len(argv) == 2:
        admin_tool = argv[1]
        # Tool argument starts from argv[2+]

        # Exmaple: admin -add username password level maxtime admin
        #            0     1      2        3      4      5      6
        # Exmaple: admin -update username new_level max_time new_admin
        if admin_tool == "-add":
            if len(argv) == 7:
                createResp = CRUD.CreateUser(argv[2], argv[3], argv[4], argv[5], argv[6])
                socket.send(str(createResp).encode())
            else:
                socket.send("[x] Error, Invalid Argument\r\nUsage: admin -add <username> <password> <level(0-5)> <max_time> <admin>(0-2)>\r\n".encode())
        elif admin_tool == "-update":
            if len(argv) == 6:
                updateResp = CRUD.updateUser(argv[2], argv[3], argv[4], argv[5])
                socket.send(str(updateResp).encode())
            else:
                socket.send("[x] Error, Invalid Argument\r\nUsage: admin -update <username> <new_level(0-5)> <max_time> <new_admin(0-2)>\r\n".encode())
        elif admin_tool == "-remove":
            if len(argv) == 3:
                rmResp = CRUD.RemoveUser(argv[2])
                socket.send(str(rmResp).encode())
            else:
                socket.send("[x] Error, Invalid Argument\r\nUsage: admin -remove <username>\r\n".encode())
        elif admin_tool == "find_user":
            if len(argv) == 3:
                usrResp = CRUD.GetUser(argv[2])
                usrResp = usrResp.replace(",", "\r\n")
                socket.send(str(usrResp).encode())
        elif admin_tool == "-motd":
            if len(argv) >= 3:
                motd = utils.arr2str(argv, " ").replace(f"{argv[0]} {argv[1]}", "")
                motdResp = utils.change_motd(motd)
                socket.send(str(motdResp).encode())

    else:
        socket.send("[x] Error, Invalid Argument.\r\n".encode())
            

