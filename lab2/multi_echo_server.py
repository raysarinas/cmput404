#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # create TCP socket
    
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # SO_REUSEADDR - echos back to client?
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2) # how many can wait in queue
        
        #continuously listen for connections - no exit clause because it is a server
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            p = Process(target=handle_echo, args=(addr, conn))
            p.daemon = True
            p.start()
            print("Started process ", p)

            # p.join()

def handle_echo(addr, conn):
    print("Connected by ", addr)

    # recieve data, then send it back
    full_data = conn.recv(BUFFER_SIZE)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()


if __name__ == "__main__":
    main()
