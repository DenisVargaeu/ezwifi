from utils import print_header
from colorama import Fore
import socket
from InquirerPy import inquirer

def run_dns_lookup():
    domain = inquirer.text(message="Enter domain for DNS lookup:").execute()
    if not domain:
        return
    print_header(f"DNS LOOKUP for {domain}")
    try:
        ip_addr = socket.gethostbyname(domain)
        print(f"Domain: {Fore.YELLOW}{domain}")
        print(f"IP: {Fore.YELLOW}{ip_addr}")
    except Exception:
        print("Failed to resolve IP.")