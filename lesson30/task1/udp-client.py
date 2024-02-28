import socket

HOST = "127.0.0.1"
PORT = 3000
msg = b'hello world'

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(msg, (HOST, PORT))