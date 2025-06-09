import paramiko

HOST = "localhost"  # Replace after testing
PORT = 2222
USERNAME = "kali"

def try_ssh():
    password = "kali"  # Static password for now
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOST, port=PORT, username=USERNAME, password=password, timeout=5)
        print(f"[+] Password found: {password}")
        
        while True:
            cmd = input(">")
            if cmd.strip().lower() == "exit":
                print("[*] Exiting session.")
                client.close()
                break

            stdin, stdout, stderr = client.exec_command(cmd)
            output = stdout.read().decode()
            error = stderr.read().decode()

            print("[Output]")
            print(output if output else "(No output)")
            if error:
                print("[Error]")
                print(error)

    except paramiko.AuthenticationException:
        print(f"[-] Authentication failed with: {password}")
    except Exception as e:
        print(f"[!] Connection error: {e}")

# Run the function
try_ssh()
