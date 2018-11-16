import socket

TCP_IP = '192.168.50.158'           # IP address to connect to
TCP_PORT = 5005                     # Port to connect to
BUFFER_SIZE = 1024                  # Buffer size for receiving message


print ("Attempting to contact server at ",TCP_IP,":",TCP_PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)               # Establish socket
s.connect((TCP_IP, TCP_PORT))                                       # Connect on pre-determined IP and Port
print ("Connection to Server Established")

while True:
    message = input("Enter command to send to server: ")            # Get message from user
    s.sendall(str.encode(message))                                  # Encode the message to bytes and send
    data = s.recv(BUFFER_SIZE)                                      # Recive response
    if not data:                                                    # If response is empty, end connection
        break
    print(data.decode("ascii"))                                     # Else display response

print("Connection to Server Terminated")
s.close()                                                           # Close connection



