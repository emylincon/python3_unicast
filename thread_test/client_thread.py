#!/usr/bin/env python3

import socket
import os
import threading
import time

t_lock = threading.Lock()


def client():
    host = input('Server IP: ').strip()  # The server's hostname or IP address
    port = 65000        # The port used by the server

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.connect((host, port))
            while True:
                try:
                    send = 'hello'
                    t_lock.acquire()
                    s.sendall(str.encode(send))
                    t_lock.release()
                    time.sleep(1)
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

