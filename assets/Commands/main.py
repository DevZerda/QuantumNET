# Modules
import os, sys, time

# Files
from ..Auth.main import *
from ..Logger.main import *
from ..banner_system.modify import *

buffer_length = 1024

def MainScreen(socket, ip):
    socket.send("Choose an option: ".encode())
    option_dude = socket.recv(buffer_length).decode().strip().replace("\r\n", "")
    if int(option_dude) == 1:
        login(socket,ip)
    elif int(option_dude) == 2:
        register(socket,ip)
    elif int(option_dude) == 3:
        free_mode(socket, ip)
    elif int(option_dude) == 4:
        about(socket)
    else:
        socket.send("[x] Error, Invalid Argument\r\n".encode())



def login(socket, ip):
    # User Input Login Section
    socket.send("Username: ".encode())
    username = socket.recv(buffer_length).decode().strip().replace("\r\n", "")
    socket.recv(buffer_length)
    socket.send("Password: ".encode())
    password = socket.recv(buffer_length).decode().strip().replace("\r\n", "")

# Login Check
    if "[+]" in Auth.Login(username, password, ip): # This is a weird way of authentication lol 
        Current.CurrentInfo['Username'] = username
        socket.send(str(Strings.MainColors['Clear'] + BannerModify.GetBannerFromFile("main") + "\r\n" + BannerModify.GetBannerFromFile("net_stats")).encode())
        socket.send(f"Welcome to Quantum Net {username}\r\n".encode())
        MainLogger.Log(f"login: {username} | {password} {utils.CurrentTime()}", True)
        return username
    else:
        socket.send("[x] Error, Incorrect username or password. Try again....".encode())
        time.sleep(4)
        socket.close()

def register(socket, ip):
    socket.send("Username: ".encode())
    username = socket.recv(buffer_length).decode().strip().replace("\r\n","")
    socket.send("Password: ".encode())
    password = socket.recv(buffer_length).decode().strip().replace("\r\n", "")



def free_mode(socket, ip):
    return ""

def about(socket):
    return ""