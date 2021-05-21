import os, sys, time

def geo_command(socket, argv):
    socket.send("working command".encode("utf-8"))
