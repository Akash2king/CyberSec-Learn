import socket
import time

def tcp_ping(host, port=80, timeout=2):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((host, port))
        s.close()
        return True
    except:
        return False

def scan_port(host, port, timeout=1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((host, port))
        s.close()
        return True
    except:
        return False

def nmap_scan(host, start_port, end_port):
    print(f"\n[🔍] Scanning {host} ports {start_port}-{end_port}...\n")
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"[OPEN] Port {port}")
            open_ports.append(port)
    if open_ports:
        print(f"\n✅ Open ports found: {open_ports}")
    else:
        print("\n❌ No open ports found.")

def main():
    target = input("Enter target IP or domain: ")
    start_port = int(input("Enter start port for scan: "))
    end_port = int(input("Enter end port for scan: "))

    print(f"\n[🌐] Pinging {target}...")
    if tcp_ping(target):
        print(f"[✅] {target} is reachable! Starting port scan...")
        start_time = time.time()
        nmap_scan(target, start_port, end_port)
        end_time = time.time()
        print(f"\n[⏱] Scan completed in {end_time - start_time:.2f} seconds.")
    else:
        print(f"[❌] {target} is not reachable (TCP ping failed). Skipping scan.")

if __name__ == "__main__":
    main()
