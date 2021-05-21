

def help_command(socket):
    socket.send("working\r\n".encode("utf-8"))