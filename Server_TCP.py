import socket
from datetime import datetime

TCP_IP = '192.168.50.158'           # IP address to connect to
TCP_PORT = 5005                     # Port to connect to
BUFFER_SIZE = 1024                  # Buffer size for receiving message
connection = True                   # Flag to determine if to exit or end

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # Establish socket
s.bind((TCP_IP, TCP_PORT))                                  # Bind to client IP & port

while True:                                                 # Loop until connection ended
    s.listen(1)                                             # Listen for connection
    conn, addr = s.accept()                                 # Establish connection
    print("Connection to Client Established")
    print('Server Address:', TCP_IP)
    print('Client Address:', addr[0])


    while connection:                                       # Loop until end or exit
        data = conn.recv(BUFFER_SIZE)                       # Receive message from client
        if (data.decode("utf-8") == "What is the current date and time?"):          # Decode response and reply
            time = datetime.now()                                                   # Get current date and time
            message = "Current Date and Time - " + time.strftime("%m/%d/%Y %H:%M:%S")
            conn.sendall(message.encode('ascii'))                                   # Encode message and send
        elif (data.decode("utf-8") == "Exit"):
            conn.sendall(b'')                                                       # If exit, send back empty response
            connection = False                                                      # Set flag to false then break
            break
        elif (data.decode("utf-8") == "End"):
            conn.sendall(b'')                                                       # If end, send back empty response
            break                                                                   # then break
        else:
            conn.sendall(b"Error: invalid request")                                 # Reply with error message
                                                                                    # for invalid request
    if not connection:                              # Break if flag was set
        break
    print("Connection to Client Terminated")
    print("Listening for new connection\n")
    conn.close()                                    # Close connection and wait for new one


conn.close()                                        # Close connection and end program
print("Server terminated")