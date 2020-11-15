import serial
import time
 
# Open a serial connection to Roomba
ser = serial.Serial(port='/dev/serial0', baudrate=115200)
 
# Assuming the robot is awake, start passive mode. Note that 0x80 in hexadecimal corresponds to 128.
ser.write('\x80')
time.sleep(.1)

# Assuming the robot is awake, start safe mode. Note that 0x82 in hexadecimal corresponds to 130.
ser.write('\x82')
time.sleep(.1)
# Start cleaning - 135To drive in reverse at a velocity of -200 mm/s while turning at a radius of 500mm, you would send the serial byte sequence [137] [255] [56] [1] [244].
# Velocity = -200 = hex FF38 = [hex FF] [hex 38] = [255] [56] Radius = 500 = hex 01F4 = [hex 01] [hex F4] = [1] [244]
# 137
ser.write('\x89')
time.sleep(.1)
# 255
ser.write('\xFF')
time.sleep(.1)
# 56
ser.write('\x38')
time.sleep(.1)
# 1
ser.write('\x01')
time.sleep(.1)
# 244
ser.write('\xF4')
time.sleep(3)
#stop: 173
ser.write('\xAD')




# Close the serial port; we're done for now.
ser.close()
