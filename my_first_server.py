import socket

print('my first server started')

#define IP-address / port
MY_IP_ADR = "192.168.149.178"
PORT = 55555

#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind & listen
s.settimeout(15)
s.bind((MY_IP_ADR,PORT))
s.listen()

#receive & print
try:
   print('waiting for connection...')
   conn, adr = s.accept()
except:
   print('timed out!')

data = conn.recv(1024)
print(data.decode('utf8'))

#teardown
s.close()
print('leaving my first server!')

