import socket
from datetime import datetime

UDP_IP = 'X.X.X.X'
UDP_PORT = 5005
BUFFER_SIZE = 1024
connection = True


def rcvPacket():
    """
    Receive messages over UDP and respond based on the message

    Send back date and time when requested, else end or exit the session
    """""

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((UDP_IP, UDP_PORT))
        print("Server binded to ", UDP_IP, ":", UDP_PORT)

        while connection:
            data, addr = s.recvfrom(BUFFER_SIZE)

            if (data.decode("utf-8") == "What is the current date and time?"):
                time = datetime.now()
                message = "Current Date and Time - " + time.strftime("%m/%d/%Y %H:%M:%S")
                s.sendto(message.encode('ascii'), addr)

            elif (data.decode("utf-8") == "Exit"):
                s.sendto(b'', addr)
                connection = False
                break

            elif (data.decode("utf-8") == "End"):
                s.sendto(b'', addr)
                break

            else:
                s.sendto(b"Error invalid request", addr)

        if not connection:
                break

    print("Server terminated")
    s.close()


def __main__(self):
    rcvPacket()
