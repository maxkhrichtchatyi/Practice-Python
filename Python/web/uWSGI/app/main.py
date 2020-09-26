class App:
    HTTP_LINE_SEPARATOR = "\r\n"

    @staticmethod
    def parse_header_line(line):
        key, value = line.split(":", maxsplit=1)
        key = "HTTP_" + key.upper().replace("-", "_").replace(" ", "_")
        value = value.strip()
        return key, value

    def parse_request(self, raw_request):
        """
        Parse an HTTP Request into a python dictionary. Requests look like this:
        GET / HTTP/1.1
        Accept: text/html
        Host: localhost:8000
        """
        request_line, *header_lines = raw_request.split(self.HTTP_LINE_SEPARATOR)
        method, path, protocol = request_line.split()
        headers = dict(self.parse_header_line(line) for line in header_lines if line)

        return {
            "REQUEST_METHOD": method,
            "PATH_INFO": path,
            "SERVER_PROTOCOL": protocol,
            **headers,
        }

    def route(self):
        pass

    @route()
    def run(self, environ, start_response):
        """A WSGI app."""

        print(self.parse_request(environ))

        start_response("200 OK", [("Content-Type", "text/plain")])
        return [b"Hello world from a simple WSGI application!"]
