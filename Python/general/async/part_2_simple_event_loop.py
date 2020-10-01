import socket
from select import select

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

# Monitoring
descriptors_to_monitor = []


def accept_connection(server_socket):
    client_socket, client_addr = server_socket.accept()
    print("Connection from:", client_addr)
    descriptors_to_monitor.append(client_socket)


def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = "Hello from socket!\n".encode()
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop():
    while True:
        ready_to_read, ready_to_write, with_errors = select(descriptors_to_monitor, [], [])

        for descriptor in ready_to_read:
            if descriptor is server_socket:
                accept_connection(server_socket=descriptor)
            else:
                send_message(client_socket=descriptor)


if __name__ == "__main__":
    # Add the server socket to monitoring list
    descriptors_to_monitor.append(server_socket)
    event_loop()
