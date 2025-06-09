import socket
import time

def scan_port(host, port, timeout=1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((host, port))
        s.close()
        return True
    except:
        return False

def main():
    target = input("Enter target IP or domain: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    
    print(f"\nStarting scan on {target} from port {start_port} to {end_port}\n")
    start_time = time.time()
    
    open_ports = []
    for port in range(start_port, end_port + 1):

        if scan_port(target, port):
            print(f"[OPEN] Port {port}")
            open_ports.append(port)
        else:
            print(f"[CLOSED] Port {port}")
    
    end_time = time.time()
    print(f"\nScan completed in {end_time - start_time:.2f} seconds")
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
