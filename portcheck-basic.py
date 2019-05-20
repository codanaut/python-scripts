import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('192.168.1.11',8096))

if result == 0:
   print("Port is open")
else:
   print("Port is not open")