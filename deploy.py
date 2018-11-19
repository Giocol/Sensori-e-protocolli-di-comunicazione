#!/usr/bin/env python3

import sys
from time import sleep
from threading import Thread
from argparse import ArgumentParser
from socketserver import TCPServer
from http.server import SimpleHTTPRequestHandler as Handler
import webbrowser


DEFAULT_ADDR = '127.0.0.1'
DEFAULT_PORT = 8080

parser = ArgumentParser(description="Serve reveal.js slides.")
parser.add_argument('port', metavar='PORT', type=int, nargs='?',
                    default=DEFAULT_PORT)
parser.add_argument('--show', action='store_true', default=False,
                    help="Open in browser.")
arg = parser.parse_args()


def httpd_t():
    print("Serving at http://{}:{}".format(DEFAULT_ADDR, arg.port))
    s = TCPServer((DEFAULT_ADDR, arg.port), Handler)
    s.serve_forever()


def show():
    webbrowser.open("http://{}:{}/".format(DEFAULT_ADDR, arg.port))


if __name__ == '__main__':
    httpd = Thread(target=httpd_t)
    httpd.daemon = True
    httpd.start()

    if arg.show:
        show()

    try:
        while True:
            sleep(60 * 60 * 24)
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
