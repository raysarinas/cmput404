#!/usr/bin/env python3
import socket, sys

#create a tcp socket
def create_tcp_socket():
    print('Creating socket')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM creates a TCP socket
    except (socket.error, msg):
        print(f'Failed to create socket. Error code: {str(msg[0])} , Error message : {msg[1]}')
        sys.exit()
    print('Socket created successfully')
    return s

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

#send data to server
def send_data(serversocket, payload):
    print("Sending payload")    
    try:
        serversocket.sendall(payload.encode()) # send all data to all socket(s)? - question 2 # remember to encode. defined as string but over socket, need to convert into binary string?
    except socket.error:
        print ('Send failed')
        sys.exit()
    print("Payload sent successfully")

def main():
    try:
        #define address info, payload, and buffer size
        host = 'www.google.com'
        port = 80 # could be arbitrary
        payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n' # requesting page from host using GET
        buffer_size = 4096 # breaks down response into chunks - size of chunks

        #make the socket, get the ip, and connect
        s = create_tcp_socket() # make socket

        remote_ip = get_remote_ip(host) # get ip

        s.connect((remote_ip , port)) # try to connect - remember to pass as a tuple
        print (f'Socket Connected to {host} on ip {remote_ip}')
        
        #send the data and shutdown
        send_data(s, payload) # to socket
        s.shutdown(socket.SHUT_WR) # shutdown after sending - but still receiving data from socket
                ## lets socket know there is no more requests to be sent so can start getting data

        #continue accepting data until no more left
        full_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                 break
            full_data += data
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        #always close at the end!
        s.close()
if __name__ == "__main__":
    main()

