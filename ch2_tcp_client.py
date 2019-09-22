import socket

target_host = socket.gethostname()
target_port = 9999


print(target_host)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send(b"Client: Hello")
#client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
response = client.recv(4096)
client.close()
print (response.decode('ascii'))


