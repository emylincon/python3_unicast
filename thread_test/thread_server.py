#!/usr/bin/env python3

import socket
import os
import threading

t_lock = threading.Lock()


def ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def unicast_call():
    host = ip_address()
    port = 65000        # Port to listen on (non-privileged ports are > 1023)

    print('Server IP: {}'.format(host))

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            while True:
                try:
                    s.listen()
                    t_lock.acquire()
                    conn, addr = s.accept()
                    with conn:
                        # print('Connected: ', addr)
                        data = conn.recv(1024)
                        print(addr[0], ': ', data.decode())
                    t_lock.release()
                except KeyboardInterrupt:
                    print('\nexit')
                    break

    except KeyboardInterrupt:
        print('\nProgramme Forcefully Terminated')


def main():
    os.system('clear')
    print('================== Programme Active =====================\n')
    unicast_call()


if __name__ == "__main__":
    main()
