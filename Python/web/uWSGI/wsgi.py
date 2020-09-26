import socket

from app.main import App

HTTP_LINE_SEPARATOR = "\r\n"
MAX_REQUEST_BYTES = 1024


def configure_socket(server_socket, host, port):
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Now listening for connections on http://{host}:{port}")


def load_raw_request(conn):
    request_bytes = conn.recv(MAX_REQUEST_BYTES)
    return request_bytes.decode("utf-8")


def server_forever():
    app = App()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        configure_socket(server_socket, "127.0.0.1", 9003)

        while True:
            client_connection, client_address = server_socket.accept()

            with client_connection as con:
                raw_request = load_raw_request(conn=con)

                if not raw_request:
                    break

                def header_response(status, headers):
                    initial_response = HTTP_LINE_SEPARATOR.join(
                        [
                            f"HTTP/1.1 {status}",
                            *[f"{key}: {value}" for (key, value) in headers],
                            "",
                            "",
                        ]
                    )
                    initial_response_bytes = initial_response.encode("utf-8")
                    con.sendall(initial_response_bytes)


                response_chunks = app.run(raw_request, header_response)

                for chunk in response_chunks:
                    con.sendall(chunk)


if __name__ == '__main__':
    server_forever()
