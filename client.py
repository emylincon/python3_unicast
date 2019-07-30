#!/usr/bin/env python3

import socket
import os


def client():
    host = input('Server IP: ').strip()  # The server's hostname or IP address
    port = 65000        # The port used by the server

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            while True:
                send = input('Enter Message: ').strip()
                s.sendall(str.encode(send))
                if send.lower() == 'exit':
                    print('Programme Terminated')
                    break
    except KeyboardInterrupt:
        print('Programme Terminated')


def main():
    os.system('clear')
    print("================== Welcome to Client Platform ===================")
    client()


if __name__ == "__main__":
    main()

