
# ezwifi

**ezwifi** is a simple yet powerful CLI tool for Wi-Fi and network testing, written in Python.  
It offers various network utilities like showing Wi-Fi info, ping, traceroute, speedtest, DNS lookup, port scanning, and serial communication with ESP32.

---

## Features

- **-info**: Show detailed Wi-Fi information (Windows only)  
- **-ip**: Display basic IP information of your computer  
- **-ping**: Run a ping test to a chosen IP or domain  
- **-trace**: Perform a traceroute to a chosen IP or domain  
- **-speed**: Run an internet speed test  
- **-dns**: DNS lookup for a given domain name  
- **-scan**: Scan open ports on a chosen IP  
- **-esp32**: Serial communication with ESP32 (non-stable feature)  
- **-v**: Show version and author information  

---

## Installation

Requires Python 3.7+ and these libraries:

```bash
pip install colorama InquirerPy speedtest-cli pyserial click
````

---

## Usage

Download the EXE or run the script directly with Python.
then open cmd and ko to directory where is the ezwifi.exe and try some exemplase commands or you can get it into the path 
Examples:

```bash
ezwifi -info
ezwifi -ping
ezwifi -speed
ezwifi -v
```

For detailed help:

```bash
ezwifi.exe --help
```

---

## Author

Denis Varga
[denisvarga.eu](https://denisvarga.eu) | [denisvarga.com](https://denisvarga.com)

---

## Version

1.0.0 (build 11)





