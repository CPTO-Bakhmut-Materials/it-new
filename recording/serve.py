#!/usr/bin/env python3
"""Local web server for the lesson 3 practice pages (http://localhost:8765/).

Serves src/lesson-3-internet/files; a POST (the practice sign-up form) just
returns done.html, so passwords never appear in the address bar or anywhere else.
"""
import functools
import http.server
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "lesson-3-internet", "files")


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        self.rfile.read(int(self.headers.get("Content-Length", 0)))  # discard the form data
        self.path = "/done.html"
        return self.do_GET()

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    http.server.ThreadingHTTPServer(("127.0.0.1", 8765),
                                    functools.partial(Handler, directory=ROOT)).serve_forever()
