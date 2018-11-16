import socket

UDP_IP = '192.168.50.158'               # IP address to connect to
UDP_PORT = 5005                         # Port to connect to
BUFFER_SIZE = 1024                      # Buffer size for receiving message

print ("Attempting to contact server at ",UDP_IP,":",UDP_PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                # Establish socket

while True:
    message = input("Enter command to send to server: ")            # Get message from user
    s.sendto(str.encode(message), (UDP_IP, UDP_PORT))               # Encode message to bytes, send to IP & port
    data, server = s.recvfrom(BUFFER_SIZE)                          # Receive response from server
    if not data:                                                    # If no data back, end client
        break
    print(data.decode("ascii"))                                     # Print response

print("Client ended")