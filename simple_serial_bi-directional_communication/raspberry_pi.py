import serial

# Establish the connection on a specific port
ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    # Send a message to the Arduino
    ser.write(b'Hello from Raspberry Pi!\n')
    
    # Read the incoming message from the Arduino
    incoming_message = ser.readline().decode().strip()
    print('Received from Arduino: ', incoming_message)
