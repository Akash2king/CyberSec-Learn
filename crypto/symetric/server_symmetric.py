import socket
from cryptography.fernet import Fernet

# Generate and share this key securely ahead of time
key = Fernet.generate_key()
cipher = Fernet(key)

# Setup server
server = socket.socket()
server.bind(('localhost', 9999))
server.listen(1)
print("[Server] Waiting for connection...")
conn, addr = server.accept()
print(f"[Server] Connected by {addr}")

# Receive encrypted message
encrypted_msg = conn.recv(1024)
print("[Server] Encrypted:", encrypted_msg)

# Decrypt message
decrypted_msg = cipher.decrypt(encrypted_msg)
print("[Server] Decrypted:", decrypted_msg.decode())

conn.close()
