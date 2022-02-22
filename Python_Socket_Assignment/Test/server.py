from pickle import FALSE
import socket
import threading 
import time

HEADER= 64
PORT = 5050
FORMAT='utf-8'
#SERVER = socket.gethostbyname(socket.gethostname())   ## I am fetching my IPV4 address
SERVER = "192.168.1.12"
#print(socket.gethostbyname(socket.gethostname()))
#print(SERVER)

ADDR= (SERVER, PORT)
DISCONNECT_MESSAGE= "!DISCONNECT"


server =socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating the socket for the server and defining type
server.bind(ADDR)   # so we bind the socket to the address of the server; anything connect to this address will hit this socket


def handle_client(conn, addr): 
    print(f"[NEW CONNECTION] {addr} connected")

    connected=True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length= int (msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Message_received".encode(FORMAT))

    conn.close()







def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread= threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[Active Connections] {threading.activeCount() - 1}")


print("[STARTING] server is starting......")
start()



