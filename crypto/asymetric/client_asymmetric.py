import socket
import rsa

# Connect to server and get public key
client = socket.socket()
client.connect(('localhost', 9998))

public_key_data = client.recv(2048)
public_key = rsa.PublicKey.load_pkcs1(public_key_data)

# Encrypt message
message = b"Hello from client using RSA asymmetric encryption!"
encrypted_msg = rsa.encrypt(message, public_key)

# Send encrypted message
client.send(encrypted_msg)
print("[Client] Encrypted message sent.")
client.close()
