import serial
import time
from remote_control_config import{
    steer,
}
def main()
 
# Open a serial connection to Roomba
ser = serial.Serial(port='/dev/serial0', baudrate=115200)
 
# Assuming the robot is awake, start passive mode. Note that 0x80 in hexadecimal corresponds to 128.
ser.write('\x80')
time.sleep(.1)

# Assuming the robot is awake, start safe mode. Note that 0x82 in hexadecimal corresponds to 130.
ser.write('\x82')
time.sleep(.1)

direction = "left"

steer(direction, ser)

time.sleep(3)
#stop: 173
ser.write('\xAD')

# Close the serial port; we're done for now.
ser.close()

return

main()