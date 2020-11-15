import serial
import time
from remote_control_config import(
    steer,
    straight_left,
)
from keyboard_control import(
    init,
    getKey,
)
def main():
 
    # Open a serial connection to Roomba
    ser = serial.Serial(port='/dev/serial0', baudrate=115200)
     
    # Assuming the robot is awake, start passive mode. Note that 0x80 in hexadecimal corresponds to 128.
    ser.write('\x80')
    time.sleep(.1)

    # Assuming the robot is awake, start safe mode. Note that 0x82 in hexadecimal corresponds to 130.
    ser.write('\x82')
    time.sleep(.1)

    #direction = "straight-backwards"
    #direction = "straight-forwards"
    #direction = "left-forwards"
    #direction = "right-forwards"
    #direction = "right-backwards"
    #direction = "left-backwards"
    if getKey('UP') and getKey('LEFT'):
        straight_left(ser)
        print('straight-left')
    #steer(direction, ser)

    time.sleep(1)
    #stop: 173
    ser.write('\xAD')

    # Close the serial port; we're done for now.
    ser.close()

    return

if __name__ == '__main__':
	init()
	while True:
		main()
