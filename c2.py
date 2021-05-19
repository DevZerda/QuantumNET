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
port = random.randint(0, 65500)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Try To Reuse Port Bypass TIME_WAIT Sometimes
sock.bind((host, port))
sock.listen()

print(f"Quantum Started | Port: {port}")

def handle_connection(client, addr):
        Current.CurrentInfo["IP"] = addr[0]

        client.send(str(MainColors["hostname"]).encode("utf-8"))
        client.settimeout(10)
        username = client.recvfrom(1024) #fix this // does wait for response 
        password = client.recvfrom(1024) #fix this // does wait for response 
        client.send(str(username).encode("utf-8"))
        client.send(str(password).encode("utf-8"))
        while(True):
                client.send(str(MainColors["hostname"]).encode("utf-8"))
                data = client.recv(512).decode("utf-8")
                data = str(data.strip()).replace("\r\n", "") # Fix Data New Line And No Need To Go Through Whole String !
        
                if data.lower() == "help":
                        continue


def listener():
    while True:
        client, address = sock.accept()
        threading.Thread(target=handle_connection, args=(client,address)).start()
        print("\033[37mTCP Connection From\033[32m ", address)
threading.Thread(target=listener).start()
