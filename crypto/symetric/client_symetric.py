import socket
from cryptography.fernet import Fernet

# Use the same key as server
key = Fernet.generate_key()  # Replace with key from server
cipher = Fernet(key)

# Encrypt message
message = b"Hello, encrypted over socket using AES!"
encrypted_msg = cipher.encrypt(message)

# Send to server
client = socket.socket()
client.connect(('localhost', 9999))
client.send(encrypted_msg)
client.close()
