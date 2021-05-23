import requests, sys
from .Config.current import *

def CF(socket, argv):
    if len(Current.CurrentCmd[args]) == 2:
        send = (requests.get("https://webresolver.nl/api.php?key=M8GAR-4LBHP-I3WD8-S1Y0T&html=0&action=cloudflare&string=" + sys.argv[1]).text)
        info = send
        socket.send(f"{send}\r\n".encode("utf-8"))
    else:
        socket.send("Error Invalid Argument Example: cf <URL>".encode())
