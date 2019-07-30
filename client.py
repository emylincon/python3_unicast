#!/usr/bin/env python3

import socket


def client():
    host = input('Server IP: ').strip()  # The server's hostname or IP address
    port = 65000        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            send = input('Enter Message: ').strip()
            s.sendall(str.encode(send))


