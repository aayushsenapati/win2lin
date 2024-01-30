import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the hostname
host = socket.gethostname()
port = 12345

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print(f"Server is listening on {host}:{port}")

while True:
    # Accept a connection from a client
    client_socket, addr = server_socket.accept()
    print(f"Received connection from {addr}")

    # Send a message to the client
    message = "Hello from the server!"
    client_socket.send(message.encode())
    client_socket.close()
