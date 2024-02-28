import socket

HOST = '127.0.0.1'
PORT = 3033
msg = input('Enter message: ')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(msg.encode('UTF-8'))
    data = s.recv(1024)
print('Received', repr(data))