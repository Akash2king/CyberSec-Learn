import socket
import rsa
import threading

# Generate key pair for server
server_pub, server_priv = rsa.newkeys(2048)

# Start server socket
server = socket.socket()
server.bind(('localhost', 9999))
server.listen(1)
print("[Server] Waiting for connection...")
conn, addr = server.accept()
print(f"[Server] Connected to {addr}")

# Send server's public key
conn.send(server_pub.save_pkcs1())

# Receive client's public key
client_pub_data = conn.recv(2048)
client_pub = rsa.PublicKey.load_pkcs1(client_pub_data)

# Function to receive and decrypt
def receive_messages():
    while True:
        try:
            encrypted_msg = conn.recv(4096)
            decrypted_msg = rsa.decrypt(encrypted_msg, server_priv)
            print(f"[Client]: {decrypted_msg.decode()}")
        except:
            break

# Function to send encrypted messages
def send_messages():
    while True:
        msg = input("[You]: ")
        encrypted = rsa.encrypt(msg.encode(), client_pub)
        conn.send(encrypted)

# Start threads
threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
