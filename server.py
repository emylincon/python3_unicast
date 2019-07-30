#!/usr/bin/env python3

import socket
import os

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
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected: ', addr)
                while True:
                    data = conn.recv(1024)
                    print(addr[0], ': ', data.decode())
                    if data.decode().lower() == 'exit':
                        print('Programme Terminated by Client')
                        break
    except KeyboardInterrupt:
        print('\nProgramme Forcefully Terminated')


def main():
    os.system('clear')
    print('================== Programme Active =====================\n')
    unicast_call()


if __name__ == "__main__":
    main()