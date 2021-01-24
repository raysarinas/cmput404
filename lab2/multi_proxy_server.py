#!/usr/bin/env python3
import socket, time, sys
from multiprocessing import Process

HOST = 'localhost'
PORT = 8001
BUFFER_SIZE = 1024

#get host information
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host ) # pass hostname and get ip address
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip


def main():
    #define address info, payload, and buffer size
    host = 'www.google.com'
    port = 80 # could be arbitrary
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start: # create TCP socket
        print("starting proxy server")
    
        # set opt to reuse addr
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        proxy_start.bind((HOST, PORT))
        #set to listening mode
        proxy_start.listen(1) # how many can wait in queue
        
        #continuously listen for connections - no exit clause because it is a server
        while True:
            conn, addr = proxy_start.accept()
            print("Connected by", addr) # should be localhost

            # forward whatever is received on server to google and take response
            # and send it to original conn
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                print("Connecting to Google")
                remote_ip = get_remote_ip(host) # get google IP

                proxy_end.connect((remote_ip, port)) # connect to Google; port 80

                # multithread it up
                p = Process(target=handle_proxy, args=(addr, conn, proxy_end))
                p.daemon = True
                p.start()
                print("Started new process ", p)
            
            conn.close()

def handle_proxy(addr, conn, proxy_end):
    # receive data, send to google
    send_full_data = conn.recv(BUFFER_SIZE)
    print(f"Sending recieved data {send_full_data} to google")
    proxy_end.sendall(send_full_data)
    proxy_end.shutdown(socket.SHUT_WR)

    # take response from google and send it back to original conn (client)
    data = proxy_end.recv(BUFFER_SIZE)
    print(f"Sending recieved data {data} to client")
    conn.sendall(data)    

if __name__ == "__main__":
    main()
