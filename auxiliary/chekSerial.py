import serial.tools.list_ports

def get_available_ports():
    # Fetch all active serial ports
    ports = serial.tools.list_ports.comports()
    
    if not ports:
        print("No serial ports found.")
        return []
        
    print(f"Found {len(ports)} available port(s):\n")
    
    for port in ports:
        print(f"Port: {port.device}")
        print(f"  Description: {port.description}")
        print(f"  Hardware ID: {port.hwid}\n")
        
    return [port.device for port in ports]

# Run the function
active_ports = get_available_ports()
