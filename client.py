import socket
import pickle

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

p, g, a = 23, 5, 6
A = (g ** a) % p
sock.send(pickle.dumps((p, g, A)))

msg = pickle.loads(sock.recv(1024))
B = msg

K = (B ** a) % p
print("Client's calculated key:", K)

sock.close()