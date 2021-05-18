from assets.banner_system.modify import BannerModify
import socket
import sys
import os
import requests
import time
import threading
from dhooks import Webhook
import requests

from assets.Config.main import *

clear = "cls"
host = "127.0.0.1"
port = 55555
hook = Webhook("https://discord.com/api/webhooks/844148531052412968/_uiWklaFSMI79_3NcKt45ZKumn6hvktS-mUSDnwxp_H630EIK8brKi74WWdcET_6HmH1")
os.system(clear)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()

print("\033[37m[~ \033[33mWelcome to PyNet \033[37m~]")

def server_start(client):
        client.send("\x1b]0;Net\x07".encode("utf-8"))
        client.send("\r\033[37m║\033[31mPyNetC2\033[37m║>\033[97m ".encode("utf-8"))
        data = client.recv(512).decode("utf-8")
        while(True):
                if "help" in data:
                        help_menu = open("help.txt", "r")
                        client.send(help_menu)
                elif "cls" in data:
                        client.send(str.encode(MainColors["Clear"]))
                elif "exit" in data:
                        client.close()
                elif " " in data:
                        print("")
                else:
                        print("")


def listener():
    while True:
        client, address = sock.accept()
        threading.Thread(target=server_start, args=(client,)).start()
        print("\033[37mTCP Connection From\033[32m ", address)
threading.Thread(target=listener).start()