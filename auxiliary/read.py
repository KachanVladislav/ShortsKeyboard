import serial
import time

# Configure the serial port
# For Windows, use 'COM3', 'COM4', etc.
# For Linux/Mac, use '/dev/ttyUSB0' or '/dev/ttyACM0'
SERIAL_PORT = 'COM9'  
BAUD_RATE = 115200

try:
    # Open the port with a 1-second timeout so it doesn't block forever if no data arrives
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
        print(f"Connected to {SERIAL_PORT} successfully.")
        
        # Give the connection a moment to initialize (common for Arduinos)
        time.sleep(2) 
        
        while True:
            # Read a line until a newline character (\n) is received
            if ser.in_waiting > 0:
                raw_data = ser.readline()
                
                # Decode the raw bytes into a string and strip whitespace/newlines
                decoded_data = raw_data.decode('utf-8').strip()
                
                print(f"Received: {decoded_data}")
                
except serial.SerialException as e:
    print(f"Error opening or reading serial port: {e}")
except KeyboardInterrupt:
    print("\nProgram stopped by user.")