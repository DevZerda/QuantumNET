## Modules
import os, sys, time

## Files
from ..Auth.crud import *
from ..Auth.crudFunc import *
from ..utils.main import *
from ..Config.current import *

def Admin_Command(socket, argv):
    if CrudFunctions.isReseller(Current.CurrentInfo['Username']) == True or CrudFunctions.isAdmin(Current.CurrentInfo['Username']) == True or CrudFunctions.isOwner(Current.CurrentInfo['Username']) == True:
        if len(argv) > 2:
            admin_tool = argv[1]
            # Tool argument starts from argv[2+]

            # Exmaple: admin -add username password level maxtime admin
            #            0     1      2        3      4      5      6
            # Exmaple: admin -update username new_level max_time new_admin
            # Example: admin -remove username
            # Example: admin -find_user username
            # Example: admin -motd new_motd
            if admin_tool == "-add":
                if len(argv) > 4:
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
                    motd = arrUtils.arr2str(argv, " ").replace(f"{argv[0]} {argv[1]}", "")
                    motdResp = utils.changeMOTD(motd)
                    socket.send(str(motdResp).encode())
                else:
                    socket.send("[x] Error, Invalid Argument\r\nUsage: admin -motd <new_motd>\r\n")
            elif admin_tool == "-login":
                if len(argv) == 3:
                    if argv[2] == "on":
                        ##stopped here
                        return "" ##temporary
            elif admin_tool == "":
                return ""

        else:
            socket.send("[x] Error, Invalid Argument.\r\n".encode())
    else:
        socket.send("[x] Error, You aren't an admin or reseller to access this command!\r\n".encode())
                

