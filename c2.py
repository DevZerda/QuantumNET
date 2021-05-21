#
#
#@title: Quantum NET
#@since: 5/18/21
#@creator: Quantum Security Team (vl0b, Exo, clever)
#
#



## Modules
import socket, sys, os, requests, time, threading, requests, random, select, datetime
# from pytz import timezone

## Files
from assets.Config.main import *
from assets.Logger.discord import *
from assets.banner_system.modify import *
from assets.Config.current import *

buffer_length = 1024
host = "127.0.0.1"
port = random.randint(0, 65500)
# est = timezone("EST")
# timenow = datetime.datetime.now(est)
timenow = datetime.datetime.now()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Try To Reuse Port Bypass TIME_WAIT Sometimes
sock.bind((host, port))
sock.listen()

print(f"Quantum Started | Port: {port}")
DiscordFunc.netStartUp(host, port, timenow)

def handle_connection(client, addr):
        Current.CurrentInfo["IP"] = addr[0]

        client.send("Username :".encode())
        username = client.recv(buffer_length).decode()

        client.recv(1024).decode()

        client.send("Password :".encode())
        password = client.recv(buffer_length).decode()

        print(username + " | " + password)
        client.send(str(MainColors["Clear"]).encode("utf-8")) # clear screen after login
        main(client, addr)

def main(client, addr):
        client.send(MainColors["hostname"].encode("utf-8"))
        while(True):
                data = client.recv(buffer_length).decode("utf-8").strip().replace("\r\n", "")
                print(r"{}".format(data))
                if data == r"\r\n":
                        print("empty")
                        client.send(MainColors["hostname"] + "\r\n".encode("utf-8"))
                elif data == r"b'\r\n'":
                        print("empty")
                        client.send(MainColors["hostname"] + "\r\n".encode("utf-8"))
                elif r'\r\n' in data:
                        print("newline")
                        client.send(MainColors["hostname"].encode("utf-8"))
                elif data.lower() == "help":
                        client.send(("working\r\n" + MainColors["hostname"]).encode("utf-8"))
                elif " " in data:
                        main(client, addr)
                else:
                        main(client, addr)

                if client.error:
                        client.close()
                        break
                


def listener():
    while True:
        client, address = sock.accept()
        threading.Thread(target=handle_connection, args=(client,address)).start()
        print("TCP Connection From ", address)
threading.Thread(target=listener).start()
