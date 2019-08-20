#!/usr/bin/env python3

import socket
import os
import threading

t_lock = threading.Lock()


def client():
    host = input('Server IP: ').strip()  # The server's hostname or IP address
    port = 65000        # The port used by the server

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            while True:
                try:
                    t_lock.acquire()
                    s.connect((host, port))
                    send = 'hello'
                    s.sendall(str.encode(send))
                    s.close()
                    t_lock.release()
                except KeyboardInterrupt:
                    print('exit')
                    break

    except KeyboardInterrupt:
        print('Programme Terminated')


def main():
    os.system('clear')
    print("================== Welcome to Client Platform ===================")
    client()


if __name__ == "__main__":
    main()

