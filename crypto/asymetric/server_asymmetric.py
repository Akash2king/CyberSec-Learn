import socket
import rsa

# Generate RSA keys
(public_key, private_key) = rsa.newkeys(2048)

# Setup server
server = socket.socket()
server.bind(('localhost', 9998))
server.listen(1)
print("[Server] Waiting for connection...")

conn, addr = server.accept()
print(f"[Server] Connected by {addr}")

# Send public key to client
conn.send(public_key.save_pkcs1())

# Receive encrypted message
encrypted_msg = conn.recv(4096)
print("[Server] Encrypted:", encrypted_msg)

# Decrypt using private key
try:
    decrypted_msg = rsa.decrypt(encrypted_msg, private_key)
    print("[Server] Decrypted:", decrypted_msg.decode())
except Exception as e:
    print("[Server] Decryption failed:", e)

conn.close()
