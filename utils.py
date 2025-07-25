import subprocess
from colorama import Fore, init
from InquirerPy import inquirer
import platform

init(autoreset=True)
SYSTEM = platform.system()

def print_header(text):
    line = "=" * (len(text) + 4)
    print(Fore.CYAN + line)
    print(Fore.GREEN + f"| {text} |")
    print(Fore.CYAN + line)

def run_command(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True).stdout
    except Exception as e:
        return f"{Fore.RED}Error: {e}"

def get_default_gateway():
    if SYSTEM == "Windows":
        output = subprocess.getoutput("ipconfig")
        for line in output.splitlines():
            if "Default Gateway" in line and ":" in line:
                gateway = line.split(":")[-1].strip()
                if gateway:
                    return gateway
    else:
        output = subprocess.getoutput("ip route")
        for line in output.splitlines():
            if "default via" in line:
                return line.split()[2]
    return "192.168.1.1"

def ip_prompt(title):
    PREDEFINED_IPS = {
        "Google (8.8.8.8)": "8.8.8.8",
        "Cloudflare (1.1.1.1)": "1.1.1.1",
        "Router (dynamic)": get_default_gateway(),
        "Custom IP/domain": None
    }
    option = inquirer.select(
        message=f"Select IP for {title}:",
        choices=list(PREDEFINED_IPS.keys())
    ).execute()
    if option == "Custom IP/domain":
        return inquirer.text(message="Enter IP or domain:").execute()
    return PREDEFINED_IPS[option]