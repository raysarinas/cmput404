#!/usr/bin/env python3
import socket, time
from client import create_tcp_socket, get_remote_ip, send_data
from multiprocessing import Pool

HOST = ''
PORT = 8001
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connect(addr):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        # recieve data from proxy_end
        full_data = s.recv(BUFFER_SIZE)

        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()

def main():
    address = [(HOST, PORT)]
    with Pool() as p:
        p.map(connect, address * 10)

if __name__ == "__main__":
    main()