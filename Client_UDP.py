import socket

UDP_IP = 'X.X.X.X'
UDP_PORT = 5005
BUFFER_SIZE = 1024


def sendPacket():
    """
    Connect to socket and send message over UDP

    Exit when empty string is return from server
    """""

    print ("Attempting to contact server at ", UDP_IP, ":", UDP_PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Enter command to send to server: ")
        s.sendto(str.encode(message), (UDP_IP, UDP_PORT))
        data, server = s.recvfrom(BUFFER_SIZE)
        if not data:
            break
        print(data.decode("ascii"))

    print("Client ended")


def __main__(self):
    sendPacket()
