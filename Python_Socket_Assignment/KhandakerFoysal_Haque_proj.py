""" 
EECE 7374: Fundamental of Computer Networks
Professor Dimitrios Koutsonikolas

Khandaker Foysal Haque
NUID: 002191876

================================Brief Description of the Code====================

At first, I imported the socket library and then defined the port, encoding format, and address of my server. From the defined server address and port, I created a tuple 'ADDR' which will be needed to set up the TCP connection with the server. Then I created a socket and define the address family by 'socket.AF_INET', which indicates IPV4. This means, my 
socket can communicate with IPV4 addresses. 'socket.SOCK_STREAM' defines that, the created
socket communicates with TCP protocol. Then with the predefined tuple of the server address, and socket, I establish a connection with the server with the command 'client.connect(ADDR)'. Then with 'client.send', I sent my initial message 'EECE7374 INTR 002191876' with the utf-8 encoding. 

Then for the reception of the expressions from the server, I created a while loop that checks for any received message from the server. After reception of the expression, the received message is split and then the split strings are checked against  'EECE7374 EXPR' and  'EECE7374 SUCC'. To do this, I instantiate 'if ..elif ' statement where it checks whether the received string has 'EECE7374 EXPR' or 'EECE7374 SUCC' in its first two segments. 

If the received string has 'EECE7374 EXPR', I save the following integers in two variables 'a' and 'b' and then I instantiate another if elif statement to check which type of expression ('+'/'-'/'*'/'/') it contains. Depending on the type of the expression, the operation is executed, and then the result is sent back to the server with the required format and encoding.  This loop continues until I receive this string--- 'EECE7374 SUCC' 


If the received message is 'EECE7374 SUCC', it means all the received expressions are operated accurately. Thus the server sent me a flag which I receive like all other expressions with 'client.recv(4096).decode(FORMAT)' where 4096 is the buffer size and set accordingly as the server. After the flag is received, I close the connection with ' client.close()' and then exit the program. 


The received flag is "1e4753a1f6458553cfeea5e59f33471c949d4f4de5828dbf3882d52e4f061fc0"


 """


""" =======================Importing the Libraries==================================== """

import socket



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
