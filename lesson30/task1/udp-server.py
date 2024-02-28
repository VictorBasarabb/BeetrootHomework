import socket

HOST = '127.0.0.1'
PORT = 3000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    while True:
        data, addr = s.recvfrom(1024)
        print(f'Received message: {data} ')
