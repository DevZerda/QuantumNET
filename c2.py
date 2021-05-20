#
#
#@title: Quantum NET
#@since: 5/18/21
#@creator: Quantum Security Team (vl0b, Exo, clever)
#
#



## Modules
import socket, sys, os, requests, time, threading, requests, random, select, datetime
from dhooks import Webhook #<-- install this module on yo machine

## Files
from assets.Config.main import *
from assets.Logger.discord import *
from assets.banner_system.modify import *
from assets.Config.current import *

screen_l = Webhook(str(webhooks["screen_logs"])) # works fine for now
action_l = Webhook(str(webhooks["action_logs"]))
login_l = Webhook(str(webhooks["login_logs"]))
attack_l = Webhook(str(webhooks["attack_logs"]))

host = "127.0.0.1" # nvm lol
port = 5555 #random.randint(0, 65500)
timenow = datetime.datetime.now() # current time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Try To Reuse Port Bypass TIME_WAIT Sometimes
sock.bind((host, port))
sock.listen()

print(f"Quantum Started | Port: {port}")
screen_l.send(f"Quantum Started\nPort: {port}\nHost: {host}\nTime: {timenow}") # sends msg to the discord

def handle_connection(client, addr):
        Current.CurrentInfo["IP"] = addr[0]
        client.send("Username :".encode())
        username = client.recv(1024).decode()
        client.recv(1024)
        client.send("Password :".encode())
        password = client.recv(1024).decode()
        while(True):
                client.send(MainColors["hostname"].encode("utf-8"))
                client.send(str(MainColors["hostname"]).encode("utf-8"))
                data = client.recv(512).decode("utf-8").strip().replace("\r\n", "")
                print(data)
                if data.lower() == "help":
                        continue


def listener():
    while True:
        client, address = sock.accept()
        threading.Thread(target=handle_connection, args=(client,address)).start()
        print("\033[37mTCP Connection From\033[32m ", address)
threading.Thread(target=listener).start()
