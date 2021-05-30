# Modules
import os, sys, time

# Files
from ..Auth.main import *
from ..Logger.main import *
from ..banner_system.modify import *
from ..Config.main import *

buffer_length = 1024

def MainScreen(socket, ip):
    socket.send(str(BannerModify.GetBannerFromFile("main_screen")).encode())
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
        MainScreen(socket,ip)



def login(socket, ip):
    socket.send(str(Strings.MainColors['Clear']).encode())
    # User Input Login Section
    socket.send("\rUsername: ".encode())
    username = socket.recv(buffer_length).decode().strip().replace("\r\n", "")
    # socket.recv(1024)
    socket.send("\rPassword: ".encode())
    password = socket.recv(buffer_length).decode().strip().replace("\r\n", "")
    print(f"{username} | {password}")

# Login Check
    if "[+]" in Auth.Login(username, password, ip): # This is a weird way of authentication lol 
        socket.send(str(Strings.MainColors['Clear'] + CustomBannerMaker.CreateMOTD(utils.GetMOTD()) + BannerModify.GetBannerFromFile("main") + "\r\n" + BannerModify.GetBannerFromFile("net_stats")).encode())
        socket.send(f"Welcome to Quantum Net {username}\r\n".encode())
        MainLogger.Log(f"login: {username} | Time: {utils.CurrentTime()}", True)
    else:
        socket.send("[x] Error, Incorrect username or password. Try again....".encode())
        time.sleep(4)
        socket.close()
    return username

def register(socket, ip): ## Function not finished
    socket.send("Username: ".encode())
    username = socket.recv(buffer_length).decode().strip().replace("\r\n","")
    socket.send("Password: ".encode())
    password = socket.recv(buffer_length).decode().strip().replace("\r\n", "")
    Current.CurrentInfo['Username'] = username



def free_mode(socket, ip):
    return ""

def about(socket):
    return ""