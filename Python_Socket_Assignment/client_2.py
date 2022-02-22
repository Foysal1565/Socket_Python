import socket
import socket
#from socket import*
import time

HEADER= 64
PORT = 5204
FORMAT='utf-8'
DISCONNECT_MESSAGE= "!DISCONNECT"
#SERVER = "192.168.1.12"
SERVER = 'kopi.ece.neu.edu'
ADDR=(SERVER, PORT)
job = 1

client =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
first = "EECE7374 INTR 002191876"
client.send(first.encode(FORMAT))

while True:
    if job == 1:

        received_expression = client.recv(4096).decode(FORMAT)
        print(received_expression)

        list_of_tokens = received_expression.split()

        if list_of_tokens[0] == "EECE7374" and list_of_tokens[1] == "EXPR":
            a = int(list_of_tokens[2])
            b = int(list_of_tokens[4])
            print(a, b)
            if list_of_tokens[3] == '+':
                result = a + b
            elif list_of_tokens[3] == '-':
                result = a - b
            elif list_of_tokens[3] == '/':
                result = a / b
            elif list_of_tokens[3] == '*':
                result = a * b
            result = str(result)

            RSLTT = "EECE7374 RSLT" + " " + result
            print(RSLTT)

            client.send(RSLTT.encode(FORMAT))

        elif list_of_tokens[0] == "EECE7374" and list_of_tokens[1] == "SUCC":
            flag = list_of_tokens[2]
            print(f"The required flag is: {flag}")
            job =0
            client.close()
