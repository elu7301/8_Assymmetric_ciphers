import socket
import pickle

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

msg = pickle.loads(conn.recv(1024))
p, g, A = msg

b = 15
B = (g ** b) % p
conn.send(pickle.dumps(B))

K = (A ** b) % p
print("Server's calculated key:", K)

conn.close()