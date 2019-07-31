#!/usr/bin/env python3

import socket
import os
from threading import Thread


def ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def receive_data(_con, _addr):
    with _con:
        print('Connected: ', _addr)
        while True:
            data = _con.recv(1024)
            print(_addr[0], ': ', data.decode())
            if data.decode().lower() == 'exit':
                print('Programme Terminated by Client')
                break


def receive_connection():
    host = ip_address()
    port = 65000        # Port to listen on (non-privileged ports are > 1023)

    print('Server IP: {}'.format(host))

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((host, port))
                s.listen()
                conn, addr = s.accept()

                Thread(target=receive_data, args=(conn, addr)).start()
                port += 10

        except KeyboardInterrupt:
            print('\nProgramme Forcefully Terminated')
            break


def main():
    os.system('clear')
    print('================== Programme Active =====================\n')
    receive_connection()


if __name__ == "__main__":
    main()
