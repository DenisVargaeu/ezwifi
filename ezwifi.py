import click
from network import show_wifi_info, show_ip_info, run_ping, run_traceroute
from speedtest_mod import run_speedtest
from dns import run_dns_lookup
from portscan import run_port_scan
from esp32_serial import esp32_serial_mode

VERSION = "1.0.0"
BUILD = 11
AUTHOR = "Denis Varga"
WEBSITES = ["denisvarga.eu", "denisvarga.com"]

@click.command()
@click.option('-info', 'cmd_info', is_flag=True, help='Show Wi-Fi info')
@click.option('-ip', 'cmd_ip', is_flag=True, help='Show IP info')
@click.option('-ping', 'cmd_ping', is_flag=True, help='Run ping test')
@click.option('-trace', 'cmd_trace', is_flag=True, help='Run traceroute')
@click.option('-speed', 'cmd_speed', is_flag=True, help='Run speedtest')
@click.option('-dns', 'cmd_dns', is_flag=True, help='Run DNS lookup')
@click.option('-scan', 'cmd_scan', is_flag=True, help='Port scan')
@click.option('-esp32', 'cmd_esp32', is_flag=True, help='ESP32 serial mode')
@click.option('-v', 'cmd_version', is_flag=True, help='Show version info')
def cli(cmd_info, cmd_ip, cmd_ping, cmd_trace, cmd_speed, cmd_dns, cmd_scan, cmd_esp32, cmd_version):
    """ezWiFi CLI tool by Denis"""
    if cmd_version:
        click.echo(f"ezWiFi version {VERSION} build {BUILD}")
        click.echo(f"Author: {AUTHOR}")
        click.echo("Websites:")
        for site in WEBSITES:
            click.echo(f" - {site}")
    elif cmd_info:
        show_wifi_info()
    elif cmd_ip:
        show_ip_info()
    elif cmd_ping:
        run_ping()
    elif cmd_trace:
        run_traceroute()
    elif cmd_speed:
        run_speedtest()
    elif cmd_dns:
        run_dns_lookup()
    elif cmd_scan:
        run_port_scan()
    elif cmd_esp32:
        esp32_serial_mode()
    else:
        click.echo("No option given. Run with -h for help.")

if __name__ == "__main__":
    cli()