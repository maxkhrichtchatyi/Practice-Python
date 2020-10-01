import socket

HOST = 'localhost'  # The remote host
PORT = 50007  # The same port as used by the server

# AF_INET means that we'll use IPv4.
# SOCK_STREAM means that it is a TCP socket (SOCK_DGRAM means that it is a UDP socket).
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow to reuse address
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to an address and a port
server_socket.bind((HOST, PORT))

# Listen the socket
server_socket.listen()

while True:
    client_socket, client_addr = server_socket.accept()
    print("Connection from:", client_addr)

    while True:
        request = client_socket.recv(4096)

        if not request:
            break

        response = "Hello from socket!\n".encode()
        client_socket.send(response)

    client_socket.close()
