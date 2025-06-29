import socket

def scan_ports(target, ports):
    print(f"[+] Scanning {target}...")
    for port in ports:
        try:
            with socket.socket() as s:
                s.settimeout(0.5)
                s.connect((target, port))
                print(f"[OPEN] Port {port}")
        except:
            pass
