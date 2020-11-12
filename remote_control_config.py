import serial
import time

def steer (direction, ser):

    if direction == "left":
    #To drive in reverse at a velocity of -200 mm/s while turning at a radius of 500mm, 
    # #you would send the serial byte sequence [137] [255] [56] [1] [244].
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
        status = 200

    return status