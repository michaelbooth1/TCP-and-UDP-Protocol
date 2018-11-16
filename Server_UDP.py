import socket
from datetime import datetime

UDP_IP = '192.168.50.158'               # IP address to connect to
UDP_PORT = 5005                         # Port to connect to
BUFFER_SIZE = 1024                      # Buffer size for receiving message
connection = True                       # Flag to determine if to exit or end

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                # Establish socket
    s.bind((UDP_IP, UDP_PORT))                                          # Connect to client
    print("Server binded to ",UDP_IP,":",UDP_PORT)

    while connection:                                                           # Loop until exit or end
        data, addr = s.recvfrom(BUFFER_SIZE)                                    # Recive date and addr of sender

        if (data.decode("utf-8") == "What is the current date and time?"):      # Decode message and respond
            time = datetime.now()                                               # Get current date and time
            message = "Current Date and Time - " + time.strftime("%m/%d/%Y %H:%M:%S")
            s.sendto(message.encode('ascii'), addr)             # Encode and respond with date/time

        elif (data.decode("utf-8") == "Exit"):
            s.sendto(b'', addr)                                 # Send back empty response and close connection
            connection = False
            break

        elif (data.decode("utf-8") == "End"):                   # Send back empty response and wait for new connection
            s.sendto(b'', addr)
            break

        else:
            s.sendto(b"Error invalid request", addr)            # Send error message if invalid request

    if not connection:                                          # If connection flag wasn't set to false, then loop
            break

print("Server terminated")                                      # Close server
s.close()




