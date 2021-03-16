# import socket library 
import socket 

# import threading library 
import threading 

# Choose a port that is free 
PORT = 5000

# An IPv4 address is obtained 
# for the server. 
SERVER = socket.gethostbyname(socket.gethostname()) 

# Address is stored as a tuple 
ADDRESS = (SERVER, PORT) 

#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client_screen, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client_screen.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client_screen] = client_address
        Thread(target=handle_client, args=(client_screen,)).start()


def handle_client(client_screen):  # Takes client_screen socket as argument.
    """Handles a single client_screen connection."""
    name = client_screen.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client_screen.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client_screen] = name

    while True:
        msg = client_screen.recv(BUFSIZ)
        if bytes("{quit}", "utf8") in msg:
            client_screen.close()
            print(str(name)+" has diconected")
            del clients[client_screen]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break
        broadcast(msg, name+": ")

def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)
        
clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()