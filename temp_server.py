import time
import socket

print('welcome!')

PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
HOST = "192.168.0.103"  # Standard loopback interface address (localhost)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(15)
s.bind((HOST, PORT))
s.listen()


f = open('/sys/bus/w1/devices/28-012063f42433/temperature')
#print(f.readline())
#number = input('type number:')
#print(f'Your number was:{number}')

try:
    print('waiting for connection')
    conn, addr = s.accept()
except TimeoutError:
    print('Timed out')

print(f"Connected by {addr}")
    #data = conn.recv(1024)
    #print(data.decode("ASCII"))

while True:
#for i in range(int(number)):
   f.seek(0)
   temp = f.read().strip()
   print('\r'+ temp[0:2] + '.' + temp[2:] + '°C', end=' ')
   #time.sleep(0.3)
   conn.send(bytes(temp + ' ','utf8'))

f.close()
