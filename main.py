import serial
import time
from remote_control_config import(
    forward,
    backward,
    forward_left,
    forward_right,
    backward_left,
    backward_right,
    stop

)
from keyboard_control import(
    init,
    getKey,
)
def main():
 
    # Open a serial connection to Roomba
    ser = serial.Serial(port='/dev/serial0', baudrate=115200)
     
    # Assuming the robot is awake, start passive mode. Note that 0x80 in hexadecimal corresponds to 128.
    ser.write('\x80'.encode())
    #time.sleep(.1)

    # Assuming the robot is awake, start safe mode. Note that 0x82 in hexadecimal corresponds to 130.
    ser.write('\x82'.encode())
    #time.sleep(.1)

    #direction = "straight-backwards"
    #direction = "straight-forwards"
    #direction = "left-forwards"
    #direction = "right-forwards"
    #direction = "right-backwards"
    #direction = "left-backwards"
    
    if getKey('UP') and getKey('LEFT'):
        forward_left(ser)
        print('forward_left')
    if getKey('UP') and getKey('RIGHT'):
        forward_right(ser)
        print('forward_right')
    if getKey('UP') and not(getKey('RIGHT')) and not(getKey('LEFT')):
        forward(ser)
        print('forward')

    if getKey('DOWN') and getKey('LEFT'):
        backward_left(ser)
        print('backward_left')
    if getKey('DOWN') and getKey('RIGHT'):
        backward_right(ser)
        print('backward_right')
    if getKey('DOWN') and not(getKey('RIGHT')) and not(getKey('LEFT')):
        backward(ser)
        print('backward')
    if getKey('SPACE'):
        stop(ser)
        print('stop')

    #steer(direction, ser)

    time.sleep(.1)
    #stop: 173
    #ser.write('\xAD')

    # Close the serial port; we're done for now.
    #ser.close()

    return

if __name__ == '__main__':
	init()
	while True:
		main()
