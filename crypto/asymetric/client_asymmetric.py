import socket
import rsa
import threading

# Generate key pair for client
client_pub, client_priv = rsa.newkeys(2048)

# Connect to server
client = socket.socket()
client.connect(('localhost', 9999))

# Receive server's public key
server_pub_data = client.recv(2048)
server_pub = rsa.PublicKey.load_pkcs1(server_pub_data)

# Send client's public key
client.send(client_pub.save_pkcs1())

# Function to receive and decrypt
def receive_messages():
    while True:
        try:
            encrypted_msg = client.recv(4096)
            decrypted_msg = rsa.decrypt(encrypted_msg, client_priv)
            print(f"[Server]: {decrypted_msg.decode()}")
        except:
            break

# Function to send encrypted messages
def send_messages():
    while True:
        msg = input("[You]: ")
        encrypted = rsa.encrypt(msg.encode(), server_pub)
        client.send(encrypted)

# Start threads
threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
