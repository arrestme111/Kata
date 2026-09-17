"""Run a simple HTTP server with: python3 backend.py."""

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Return a JSON response for any GET request."""
        body = json.dumps({"message": "Hello from the backend!", "path": self.path}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    with ThreadingHTTPServer(("0.0.0.0", 8000), RequestHandler) as server:
        print("Listening on http://localhost:8000 (Ctrl+C to stop)", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server.")


if __name__ == "__main__":
    main()
