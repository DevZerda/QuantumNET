import requests, sys

def ping(socket):
    socket.send('\rip: '.encode('utf-8'))
    ip = socket.recv(512).decode('utf-8')
    ip = socket.recv(1024).decode('utf-8')
    output = requests.get('https://webresolver.nl/api.php?key=U9COH-VPN9V-OWJ2P-Z4745&action=ping&string=' + ip)
    socket.send(str(output.text).encode('utf-8'))
