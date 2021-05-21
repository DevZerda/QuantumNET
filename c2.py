#
#
#@title: Quantum NET
#@since: 5/18/21
#@creator: Quantum Security Team (vl0b, Exo, clever)
#
#



## Modules
from assets.utils.main import utils
import socket, sys, os, requests, time, threading, requests, random, select, datetime

## Files
from assets.Config.main import *
from assets.Config.current import *

from assets.Logger.discord import *

from assets.banner_system.modify import *

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

        client.send("Username: ".encode())
        username = client.recv(buffer_length).decode()

        client.recv(1024).decode()

        client.send("Password: ".encode())
        password = client.recv(buffer_length).decode()

        client.send(Strings.hostname("").encode("utf-8"))
        while(True):
                try:
                        data = Input(client)
                        print(r"{}".format(data))

                        ## do not remove lines 62-67 (for testing purposes)
                        if data == r"\r\n":
                                client.send(Strings.hostname("").encode("utf-8"))
                        elif data == r"b'\r\n'":
                                client.send(Strings.hostname("").encode("utf-8"))
                        elif r'\r\n' in data:
                                client.send(Strings.hostname("").encode("utf-8"))
                        elif data.lower() == "help":
                                help_command(client)
                        elif data.lower() == "geo":
                                geo_command(client)

                        if client.timeout:
                                break

                except client.error as e:
                        if e.errno == errno.ECONNRESET:
                                # Handle disconnection -- close & reopen socket etc.
                                break
                        else:
                        # Other error, re-raise
                                raise
                        break
                

def listener():
    while True:
        client, address = sock.accept()
        threading.Thread(target=handle_connection, args=(client,address)).start()
        print("\033[37mTCP Connection From\033[32m ", address)
threading.Thread(target=listener).start()

def Input(socket):
        data = socket.recv(1024).decode("utf-8").strip().replace("\r\n", "")
        if data == '': print("Empty")
        return data
