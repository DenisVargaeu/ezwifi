from utils import print_header, run_command, ip_prompt, SYSTEM
import socket

PING_CMD = ["ping", "-n", "3"] if SYSTEM == "Windows" else ["ping", "-c", "3"]
TRACE_CMD = ["tracert"] if SYSTEM == "Windows" else ["traceroute"]

def show_wifi_info():
    print_header("WI-FI INFO")
    if SYSTEM == "Windows":
        output = run_command(["netsh", "wlan", "show", "interfaces"])
        lines = [line.strip() for line in output.splitlines() if line.strip()]
        print("\n".join(lines))
    else:
        print("Only available on Windows.")

def show_ip_info():
    print_header("IP INFORMATION")
    try:
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        print(f"PC name: {hostname}")
        print(f"IP address: {ip_addr}")
    except Exception:
        print("Failed to get IP address.")

def run_ping():
    target = ip_prompt("PING")
    if not target:
        return
    print_header(f"PING to {target}")
    output = run_command(PING_CMD + [target])
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    print("\n".join(lines))

def run_traceroute():
    target = ip_prompt("TRACEROUTE")
    if not target:
        return
    print_header(f"TRACEROUTE to {target}")
    output = run_command(TRACE_CMD + [target])
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    print("\n".join(lines))