import socket
target = input("Enter host (e.g., scanme.nmap.org or 127.0.0.1): ")

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # timeout after 1 second
        result = sock.connect_ex((host, port))  # 0 = open, else closed
        sock.close()
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
    except:
        print(f"Port {port}: ERROR")

print(f"\nScanning host: {target}\n")

# Common ports (you can expand this later)
common_ports = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]

for port in common_ports:
    scan_port(target, port)


import socket

# Ask for user input
target = input("Enter host (e.g., scanme.nmap.org or 127.0.0.1): ")

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
    except Exception as e:
        print(f"Port {port}: ERROR ({e})")

print(f"\nScanning host: {target}\n")

common_ports = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]

for port in common_ports:
    scan_port(target, port)
