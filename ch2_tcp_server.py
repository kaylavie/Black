import socket
import threading

bind_ip = socket.gethostname()
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print ("[*] Listening on", bind_ip,":",bind_port)

# client handling thread
def handle_client(client_socket):
    request  = client_socket.recv(1024)
    print ("[*] Received: ", request.decode('ascii'))

    client_socket.send(b"Server: Hello")
    client_socket.close()

while True:
    client,addr= server.accept()
    print ("[*] Accepted connection from :", addr[0],addr[1])
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
