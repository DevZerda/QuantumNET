#
#
# @title: Quantum NET
# @since: 5/18/21
# @creator: Quantum Security Team (vl0b, Exo, clever, Max, Beta)
#
#

# Modules
import socket
import sys
import os
import requests
import time
import threading
import requests
import random
import datetime

# Files
from assets.Config.main import *
from assets.Config.current import *
from assets.Auth.main import *
from assets.Auth.crud import *
from assets.Auth.crudFunc import *
from assets.Logger.main import *
from assets.Logger.discord import *
from assets.banner_system.modify import *
from assets.utils.main import utils

# Commands
from assets.Commands.help import *
from assets.Commands.methods import *
from assets.Commands.geo import *
from assets.Commands.cf import *
from assets.Commands.admin import *
from assets.Commands.playboy import *
from netControl.get_usage import *

# if utils.GetOS() == True:
#         if utils.CheckForPython3Unix() == True:
#                 print("Thanks for using python3!")
#         else:
#                 print("Must use Python3!\r\nUsage: python3 " + sys.argv[0])
#                 exit()
# else:
#         print("This is currently for LINUX!")
#         exit()

buffer_length = 1024 # We Set The Buffer Over Here So It Can Be Reused So Use It Stop Typing 1024
host = "0.0.0.0"
timenow = datetime.datetime.now()
port = random.randint(0, 65535)
if len(sys.argv) == 2:
    if sys.argv[1] == "-on":
        host = requests.get("https://api.ipify.org").text

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Try To Reuse Port Bypass TIME_WAIT Sometimes
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen()

print(f"[{datetime.datetime.now()}] | Quantum Started | {host} | {port} |") # Added Date And Time So You Can See When Was The Last Time The Net Started !


def handle_connection(client, addr):
    utils.set_Title(client, "Login")

    # User Input Login Section
    client.send("Username: ".encode())
    username = client.recv(buffer_length).decode().strip().replace("\r\n", "")
    # client.recv(1024).decode()
    client.send("Password: ".encode())
    password = client.recv(buffer_length).decode().strip().replace("\r\n", "")

    client.send(f"{username} | {password}\r\n".encode())
    client.send("Welcome to Quantum Net\r\n".encode())

    # Login Check
    if "[+]" in Auth.Login(username, password, addr[0]): # This is a weird way of authentication lol 
        client.send(f"Welcome: {username}\r\n".encode())
        client.send(str(Strings.MainColors['Clear'] + BannerModify.GetBannerFromFile("main")).encode())
        MainLogger.Log(f"login: {username} | {password} {utils.CurrentTime()}", True)
    else:
        client.send("[x] Error, Incorrect username or password. Try again....".encode())
        time.sleep(4)
        client.close()

    utils.set_Title(client, f"Quantum NET | User: {username}")

    while(True):
        client.send(Strings.hostname(username).encode())
        data = str(client.recv(buffer_length).decode()).strip().replace("\r\n", "")

        # Command Handling
        if data != "\r\n":
                Current.CurrentCmd["args"] = data.split(" ")
                # Current.CurrentCmd['Cmd'] = data[0]
                Current.CurrentCmd["fullcmd"] = data
                Current.CurrentInfo['Username'] = username

        client.send(str(Strings.MainColors['Clear'] + BannerModify.GetBannerFromFile("main")).encode())

        if data.lower() == "help" or data.lower() == "?":
                client.send(str(BannerModify.GetBannerFromFile("help")).encode())
        elif data.lower() == "clear" or data.lower() == "cls":
                client.send(str(BannerModify.GetBannerFromFile("main")).encode())
        elif data.lower() == "methods":
                client.send(str(BannerModify.GetBannerFromFile("methods")).encode())
        elif data.lower() == "api_status":
                client.send(str(BannerModify.GetBannerFromFile("api_status")).encode())
        elif data.lower() == "playboy":
                client.send(str(BannerModify.GetBannerFromFile("playboy")).encode())     
        elif data.lower() == "usage":
                client.send(str(Usage.Usage()).encode())
        elif data.lower().startswith("geo"):
                geo_command(client, Current.CurrentCmd["args"])
        elif data.lower().startswith("pscan"):
                pScan_command(client, Current.CurrentCmd['args'])
        elif data.lower().startswith("admin"):
                Admin_Command(client, Current.CurrentCmd['args'])
        if data != "\r\n":
                MainLogger.Log("CMD", True)


def listener():
    while True:
        client, address = sock.accept()
        threading.Thread(target=handle_connection, args=(client, address)).start()
        print(Strings.MainColors['Red'] + "TCP Connection From " + address[0] + ":" + str(address[1]) + Strings.MainColors['Reset'])


threading.Thread(target=listener).start()
