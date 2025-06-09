import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('20.207.70.99', 12345))
while True:
    data = s.recv(1024).decode()
    if not data:
        break
    print(data)
    print("----------")
    s.sendall(input("enter the message :").encode())

s.close()