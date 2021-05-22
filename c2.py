#
#
#@title: Quantum NET
#@since: 5/18/21
#@creator: Quantum Security Team (vl0b, Exo, clever, Max)
#
#



## Modules
import socket, sys, os, requests, time, threading, requests, random, select, datetime

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


buffer_length = 1024
host = "127.0.0.1" # requests.get("https://api.ipify.org").text
port = random.randint(0, 65500)
timenow = datetime.datetime.now() # current time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Try To Reuse Port Bypass TIME_WAIT Sometimes
sock.bind((host, port))
sock.listen()

print(f"Quantum Started | Port: {port}")
DiscordFunc.netStartUp(host, port, timenow)

def handle_connection(client, addr):
        Current.CurrentInfo["IP"] = addr[0]

        recData = client.recv(buffer_length).decode().split(":")
        if len(recData) <= 1:
                client.send("Failed to connect!".encode())
                print(Strings.MainColors["Red"] + "Connection closed, by " + addr[0] + ":" + str(addr[1]) + ""+ Strings.MainColors["Reset"])
                client.close()
                return
        username = recData[0]
        password = recData[1]
        
        client.send("1".encode())

        while(True):
                try:
                        client.send(Strings.hostname("").encode())
                        data = client.recv(buffer_length).decode()

                        ## do not remove lines 62-67 (for testing purposes)
                        # if data == r"\r\n":
                        #         client.send(Strings.hostname("").encode("utf-8"))
                        # elif data == r"b'\r\n'":
                        #         client.send(Strings.hostname("").encode("utf-8"))
                        # elif r'\r\n' in data:
                        #         client.send(Strings.hostname("").encode("utf-8"))
                        if data.lower() == "help":
                                help_command(client)
                                continue
                        elif data.lower() == "geo":
                                geo_command(client)

                        # print(client.error)

                        # if client.timeout:
                        #         break

                        if client.error:
                                continue

                except:
                        break
                

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
