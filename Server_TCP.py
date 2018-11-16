import socket
from datetime import datetime

TCP_IP = 'X.X.X.X'
TCP_PORT = 5005
BUFFER_SIZE = 1024
connection = True


def rcvPacket():
    """
    Receive messages over TCP and respond based on the message

    Send back date and time when requested, else end or exit the session
    """""

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))

    while True:
        s.listen(1)
        conn, addr = s.accept()
        print("Connection to Client Established")
        print('Server Address:', TCP_IP)
        print('Client Address:', addr[0])

        while connection:
            data = conn.recv(BUFFER_SIZE)
            if (data.decode("utf-8") == "What is the current date and time?"):
                time = datetime.now()
                message = "Current Date and Time - " + time.strftime("%m/%d/%Y %H:%M:%S")
                conn.sendall(message.encode('ascii'))
            elif (data.decode("utf-8") == "Exit"):
                conn.sendall(b'')
                connection = False
                break
            elif (data.decode("utf-8") == "End"):
                conn.sendall(b'')
                break
            else:
                conn.sendall(b"Error: invalid request")

        if not connection:
            break
        print("Connection to Client Terminated")
        print("Listening for new connection\n")
        conn.close()

    conn.close()
    print("Server terminated")


def __main__(self):
    rcvPacket()
