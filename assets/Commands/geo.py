import os, sys, time, requests, json

def geo_command(socket, argv):
    if len(argv) == 2:
        jsonResp = (requests.get("http://extreme-ip-lookup.com/json/" + argv[1]).text)
        fix = jsonResp.replace("\",\"", "\r\n")
        fix2 = fix.replace("\"", "")
        fix3 = fix2.replace("{", "")
        responsee = fix3.replace("}", "")
        socket.send(f"{responsee}\r\n".encode("utf-8"))
    else:
        socket.send("[x] Error, Invalid Arugment\r\nUsage: geo <ip>")
