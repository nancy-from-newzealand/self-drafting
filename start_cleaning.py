import serial
import time
 
# Open a serial connection to Roomba
ser = serial.Serial(port='/dev/serial0', baudrate=115200)
 
# Assuming the robot is awake, start safe mode. Note that 0x80 in hexadecimal corresponds to 128.
ser.write('\x80')
 
time.sleep(.1)
 
# Start cleaning - 135
ser.write('\x87')

time.sleep(2)

# Stop (back to off mode) - 135
ser.write('\x87')
 
# Close the serial port; we're done for now.
ser.close()
