import socket

targetIP = input('What is the target\'s IP: ')
targetPort = int(input('What port would you like to scan: '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
status = s.connect_ex((targetIP, targetPort))

if (status == 0):
  print('Port', targetPort, 'is open.')
else:
  print('Port', targetPort, 'is closed.')
  
s.close()
