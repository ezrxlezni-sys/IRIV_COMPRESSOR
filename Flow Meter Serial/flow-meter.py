import serial
import struct
import time

# ---------- Configuration ----------
PORT = "/dev/ttyUSB0"          # Change to your serial port
BAUDRATE = 9600
SLAVE_ID = 1
INTERVAL = 7                  # Seconds between successful readings
MAX_RETRIES = 5                # Retries per cycle if response is incomplete
print ("This is flow meter checking modbus serial communication bytes")
print ("Code by EZ Industry")
# -----------------------------------

def crc16_modbus(data):
    """Calculate Modbus CRC16."""
    crc = 0xFFFF
    for pos in data:
        crc ^= pos
        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc

def build_read_request(slave_id, start_addr, num_regs):
    """Build Modbus RTU request: read holding registers."""
    request = struct.pack('>B B H H', slave_id, 0x03, start_addr, num_regs)
    crc = crc16_modbus(request)
    request += struct.pack('<H', crc)
    return request

def get_response():
    """Send request and read response. Returns raw bytes."""
    request = build_read_request(SLAVE_ID, start_addr=0, num_regs=14)
    print("Request (hex):", " ".join(f"{b:02X}" for b in request))

    try:
        ser = serial.Serial(PORT, BAUDRATE, timeout=2)  # 2 sec timeout
        ser.write(request)
        time.sleep(0.2)  # Allow device time to respond

        expected_len = 5 + 2 * 14  # 33 bytes total
        response = ser.read(expected_len)
        ser.close()
        return response
    except serial.SerialException as e:
        print(f"Serial error: {e}")
        return b''

def validate_response(response):
    """Check if response is complete (33 bytes)."""
    expected_len = 5 + 2 * 14
    return len(response) == expected_len

if __name__ == "__main__":
    print(f"Starting continuous polling every {INTERVAL} seconds.")
    print(f"Will retry up to {MAX_RETRIES} times if response is incomplete.")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            success = False
            for attempt in range(1, MAX_RETRIES + 1):
                response = get_response()
                print(f"Attempt {attempt} - Response (hex):", " ".join(f"{b:02X}" for b in response) if response else "(no data)")

                if validate_response(response):
                    print(f"✅ Valid 33-byte response received!")
                    print("-" * 50)
                    success = True
                    break
                else:
                    print(f"Incomplete response: {len(response)} bytes (expected 33). Retrying...")
                    time.sleep(1)  # Short pause before retry

            if not success:
                print(f"Max retries reached. No valid response. Waiting {INTERVAL} seconds before next cycle.")
                print("-" * 50)

            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print("\nPolling stopped by user.")
