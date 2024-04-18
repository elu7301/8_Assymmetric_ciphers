import socket
import pickle
import random

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

p, g = random.randint(2, 73), random.randint(2, 73)
a = random.randint(2, 10)
A = (g ** a) % p
sock.send(pickle.dumps((p, g, A)))

msg = pickle.loads(sock.recv(1024))
B = msg

K = (B ** a) % p
print("Client's calculated key:", K)

sock.close()