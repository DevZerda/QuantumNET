import requests, sys
from .Config.current import *

def CF():
    if len(Current.CurrentCmd[args]) == 2:
        socket.send('https://webresolver.nl/api.php?key=M8GAR-4LBHP-I3WD8-S1Y0T&html=0&action=cloudflare&string='.encode('utf-8'))
