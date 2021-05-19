#
#
#@title: Quantum NET
#@since: 5/18/21
#@creator: Quantum Security Team (vl0b, Exo, clever)
#
#



## Modules
import socket, sys, os, requests, time, threading, requests, random, select

## Files
from assets.Config.main import *
from assets.banner_system.modify import *
from assets.Config.current import *

host = "127.0.0.1" #requests.get("https://api.ipify.org").text | api = requests.get("https://api.hackertarget.com/geoip/?q=" + geoip) | api = requests.get("https://api.hackertarget.com/nmap/?q=" + nmap)
port = 5555 #random.randint(0, 65500)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Try To Reuse Port Bypass TIME_WAIT Sometimes
sock.bind((host, port))
sock.listen()

print(f"Quantum Started | Port: {port}")

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
