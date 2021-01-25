import socket

targetIP = input('What is the target's IP: ')
port = input('What port would you like to scan: ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
status = s.connect_ex((target, port))

if (status == 0):
  print('Port ', port, ' is open.')
else:
  print('Port ', port, ' is closed.')
  
s.close()
