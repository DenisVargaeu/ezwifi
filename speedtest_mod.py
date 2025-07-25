import speedtest
from utils import print_header
from colorama import Fore

def run_speedtest():
    print_header("SPEEDTEST")
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        down = st.download() / 1_000_000
        up = st.upload() / 1_000_000
        ping_val = st.results.ping
        print(f"{Fore.YELLOW}Download: {down:.2f} Mbps")
        print(f"{Fore.YELLOW}Upload: {up:.2f} Mbps")
        print(f"{Fore.YELLOW}Ping: {ping_val:.1f} ms")
    except Exception as e:
        print(f"Error: {e}")