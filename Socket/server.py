import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 12345))

s.listen()

client, addr = s.accept()
print('Got connection from', addr)
while True:
    data = input("enter your message :")
    client.sendall(str.encode(data))
    data = client.recv(1024).decode()
    print("------------")
    print("message received from client is: ", data)
    print("------------")
    if data == "exit":
        break
client.close()
