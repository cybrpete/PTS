import socket

HOST = input("Server IP: ")
PORT = int(input("Server Port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Host connected with address:', HOST)

MSG = bytes(input("Enter message to send: "), 'utf-8')
s.sendall(MSG)
s.close()
