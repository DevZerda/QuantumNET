import os, sys, time, requests

def pScan_command(socket, argv):
    if len(argv) == 2:
        ports = requests.get(f"api={argv[1]}").text()
        socket.send(str(ports).encode())
    else:
        socket.send("[x] Error, Invalid Argument\r\nUsage: pscan <ip>")

def ColorScannerResult():
    return ""