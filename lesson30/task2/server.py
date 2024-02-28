import socket

HOST = '127.0.0.1'  # localhost
PORT = 3033


def caesar_cipher(data: bytes, shift: int) -> bytes:
    encrypted_data = bytearray()

    for byte in data:
        if 65 <= byte <= 90:
            encrypted_data.append((byte - 65 + shift) % 26 + 65)
        elif 97 <= byte <= 122:
            encrypted_data.append((byte - 97 + shift) % 26 + 97)
        else:
            encrypted_data.append(byte)
    return bytes(encrypted_data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            received_data = conn.recv(1024)
            if not received_data:
                break
            print(f'received: {received_data}')
            encrypted = caesar_cipher(received_data, 1)
            conn.sendall(encrypted)
            print(f'sent: {encrypted}')