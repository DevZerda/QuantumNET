import socket, sys, os


def connect(PORT):
    if PORT:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(("127.0.0.1", PORT))
            sock.send("username:password".encode())
            if sock.recv(1024).decode() == "1":
                while(True):
                    try:
                        rec = sock.recv(1024).decode()
                        ui = input(rec)
                        print(send(ui, sock))
                    except:
                        break;

def send(data, sock):
    sock.send(data.encode())
    return sock.recv(1024).decode()


connect(int(sys.argv[1]))