from guizero import *
import socket
import time

HOST = "192.168.0.103" #Host to connect to
PORT = 65432 		#Listen port

def update_text():
    data = s.recv(1024)
    data = data.decode('utf8').split(' ')
    temp = data[0]
    text.value = str(int(temp)/1000) + ' ℃'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(f"Connected by {HOST}")

#skapar ett huvud-fönster (som är osynligt till att börja med)
app = App()

#arrangera och förse vårt fönster med "liv"
text = Text(app, text=' ', size=150)
text.repeat(1000, update_text)
app.display() #kommer ej returnera förrän fönstret stängts
	
s.close()