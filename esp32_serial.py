from colorama import Fore
import serial
import serial.tools.list_ports
from InquirerPy import inquirer

def esp32_serial_mode():
    print(Fore.CYAN + "="*20)
    print(Fore.GREEN + "| Select ESP32 COM port |")
    print(Fore.CYAN + "="*20)
    ports = serial.tools.list_ports.comports()
    port_list = [port.device for port in ports]
    if not port_list:
        print(Fore.RED + "⚠️  No COM ports found.")
        return
    port_list.append("Cancel")
    chosen_port = inquirer.select(
        message="Choose COM port for ESP32:",
        choices=port_list
    ).execute()
    if chosen_port == "Cancel":
        print(Fore.YELLOW + "Port selection cancelled.")
        return

    print(Fore.GREEN + f"Opening COM port: {chosen_port} ...")

    try:
        ser = serial.Serial(port=chosen_port, baudrate=115200, timeout=1)
        print(Fore.GREEN + f"COM port {chosen_port} opened, baudrate 115200.")
        print(Fore.CYAN + "Waiting for 'ESP32: 8 - Wi-Fi Info' message before enabling input...")

        while True:
            while ser.in_waiting > 0:
                data = ser.readline().decode(errors='ignore').strip()
                if data:
                    print(Fore.YELLOW + f"ESP32: {data}")
                    if "8 - Wi-Fi Info" in data:
                        print(Fore.GREEN + "Message received! You can now type commands. Type 'exit' to quit.")
                        raise StopIteration

    except StopIteration:
        pass
    except Exception as e:
        print(Fore.RED + f"Error opening COM port: {e}")

    try:
        while True:
            while ser.in_waiting > 0:
                data = ser.readline().decode(errors='ignore').strip()
                if data:
                    print(Fore.YELLOW + f"ESP32: {data}")

            user_input = input("You > ")
            if user_input.lower() == "exit":
                print(Fore.GREEN + "Closing communication and port.")
                break

            ser.write((user_input + "\n").encode())

        ser.close()
        print(Fore.GREEN + "COM port closed.")
    except Exception as e:
        print(Fore.RED + f"Error during communication: {e}")