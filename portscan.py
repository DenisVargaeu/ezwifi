from utils import print_header, ip_prompt
from colorama import Fore
import socket

def format_ports(ports, per_line=10):
    lines = []
    for i in range(0, len(ports), per_line):
        chunk = ports[i:i+per_line]
        line = " ".join(f"{p:5d}" for p in chunk)
        lines.append(line)
    return "\n".join(lines)

def run_port_scan():
    target = ip_prompt("PORT SCAN")
    if not target:
        return
    print_header(f"PORT SCAN: {target}")
    open_ports = []
    try:
        for port in range(20, 1025):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.1)
                if sock.connect_ex((target, port)) == 0:
                    open_ports.append(port)
    except Exception as e:
        print(f"Error: {e}")
        return

    if open_ports:
        print(Fore.YELLOW + "Open ports:")
        print(Fore.YELLOW + format_ports(open_ports))
    else:
        print("No open ports found.")