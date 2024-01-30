import socket
import time

def connect_to_server():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the hostname of the server
    host = "server-container"  # Use the server container's name or IP address
    port = 12345

    
    try:
        # Connect to the server
        client_socket.connect((host, port))

        while True:
            # Receive data from the server
            message = client_socket.recv(1024)
            if not message:
                break  # Exit the inner loop if the server connection is closed
            print(f"Received from server: {message.decode()}")

    except ConnectionRefusedError:
        print("Server not available. Retrying in 5 seconds...")
        time.sleep(5)  # Wait for 5 seconds before trying to reconnect

    finally:
        client_socket.close()

if __name__ == "__main__":
    while True:
        connect_to_server()

