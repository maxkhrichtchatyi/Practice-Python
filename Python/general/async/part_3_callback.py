import socket
import selectors

selector = selectors.DefaultSelector()

HOST = 'localhost'  # The remote host
PORT = 50007  # The same port as used by the server


def server(host, port):
    # AF_INET means that we'll use IPv4.
    # SOCK_STREAM means that it is a TCP socket (SOCK_DGRAM means that it is a UDP socket).
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow to reuse address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to an address and a port
    server_socket.bind((host, port))

    # Listen the socket
    server_socket.listen()

    # Register event for server socket descriptor
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(server_socket):
    client_socket, client_addr = server_socket.accept()
    print("Connection from:", client_addr)

    # Register event for client socket descriptor
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)


def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = "Hello from socket!\n".encode()
        client_socket.send(response)
    else:
        selector.unregister(fileobj=client_socket)
        client_socket.close()


def event_loop():
    while True:
        events = selector.select()

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == "__main__":
    server(host=HOST, port=PORT)
    event_loop()
