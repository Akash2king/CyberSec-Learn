import socket
import time

def tcp_ping(host, port, timeout=2):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        
        start_time = time.time()
        s.connect((host, port))
        end_time = time.time()
        
        s.close()
        elapsed = (end_time - start_time) * 1000  # ms
        print(f"[+] {host}:{port} is reachable! Time: {elapsed:.2f} ms")
    except socket.timeout:
        print(f"[-] {host}:{port} timed out after {timeout} seconds")
    except socket.error as e:
        print(f"[-] {host}:{port} unreachable. Error: {e}")

if __name__ == "__main__":
    target_host = input("Enter host (IP or domain): ")
    target_port = int(input("Enter port (e.g., 80, 443): "))
    
    while True:
        tcp_ping(target_host, target_port)
        time.sleep(1)  # wait 1 second before next ping
