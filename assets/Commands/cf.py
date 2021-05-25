import requests, sys

def cloudflare_resolve(socket):
	socket.send("\rHost: ".encode("utf-8"))
	backend = socket.recv(512).decode("utf-8")
	backend = socket.recv(1024).decode("utf-8")
	response = requests.get("https://webresolver.nl/api.php?key=M8GAR-4LBHP-I3WD8-S1Y0T&html=0&action=cloudflare&string=" + backend)
	socket.send(str(response.text).encode("utf-8"))
