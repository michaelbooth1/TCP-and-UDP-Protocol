import socket

TCP_IP = 'X.X.X.X'
TCP_PORT = 5005
BUFFER_SIZE = 1024


def sendPacket():
    """
    Connect to socket and send message over TCP

    Exit when empty string is return from server
    """""

    print ("Attempting to contact server at ", TCP_IP, ":", TCP_PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    print ("Connection to Server Established")

    while True:
        message = input("Enter command to send to server: ")
        s.sendall(str.encode(message))
        data = s.recv(BUFFER_SIZE)
        if not data:
            break
        print(data.decode("ascii"))

    print("Connection to Server Terminated")
    s.close()


def __main__(self):
    sendPacket()
