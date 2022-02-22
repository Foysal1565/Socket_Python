""" =======================Importing the Libraries==================================== """

import socket
import socket             
#from socket import*
import time


""" ========Defining port, encode/decode format, and server tupple ============== """

PORT = 5204
FORMAT='utf-8'
SERVER = 'kopi.ece.neu.edu'
ADDR=(SERVER, PORT)


""" ===============Initializing connection to the server by sending my NUID 
                            with appropriate header================================== """

client =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
first = "EECE7374 INTR 002191876"
client.send(first.encode(FORMAT))


""" ===================== Receive Expression and return the solution=============
================================until you receive success flag============== """

while True:
    received_expression = client.recv(4096).decode(FORMAT)
    print(received_expression)

    list_of_tokens = received_expression.split()

    if list_of_tokens[0] == "EECE7374" and list_of_tokens[1] == "EXPR":
        a = int(list_of_tokens[2])
        b = int(list_of_tokens[4])
        
        if list_of_tokens[3] == '+':
            result = a + b
            print("Let's perform  addition")

        elif list_of_tokens[3] == '-':
            result = a - b
            print("Let's perform  Substraction")

        elif list_of_tokens[3] == '/':
            result = a / b
            print("Let's perform Division")

        elif list_of_tokens[3] == '*':
            result = a * b
            print("Let's perform Multiplication")


        result = str(result)

        RSLTT = "EECE7374 RSLT" + " " + result
        print("The result is:"+ str(result) + "\n")

        client.send(RSLTT.encode(FORMAT))


##==========================Flag received =====================================

    elif list_of_tokens[0] == "EECE7374" and list_of_tokens[1] == "SUCC":
        flag = list_of_tokens[2]
        print("\n" + f"The required flag is: {flag}") 
        print("\n" + "Closing the connection and Exiting program .....................") 
        client.close()
        exit()
