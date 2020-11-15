import serial
import time

def steer (direction, ser):

    if direction == "straight-forwards":
    #To drive in reverse at a velocity of -200 mm/s while turning at a radius of 500mm, 
    # #you would send the serial byte sequence [137] [255] [56] [1] [244].
    # Velocity = -200 = hex FF38 = [hex FF] [hex 38] = [255] [56] Radius = 500 = hex 01F4 = [hex 01] [hex F4] = [1] [244]

        # 137
        ser.write('\x89')
        time.sleep(.1)
        # 255
        ser.write('\x00')
        time.sleep(.1)
        # 56
        ser.write('\x64')
        time.sleep(.1)
        # 1
        ser.write('\x7F')
        time.sleep(.1)
        # 244
        ser.write('\xFF')
        status = 200

    if direction == "straight-backwards":
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
        ser.write('\x9C')
        time.sleep(.1)
        # 1
        ser.write('\x7F')
        time.sleep(.1)
        # 244
        ser.write('\xFF')
        status = 200

    if direction == "left-forwards":
    #To drive in reverse at a velocity of -200 mm/s while turning at a radius of 500mm, 
    # #you would send the serial byte sequence [137] [255] [56] [1] [244].
    # Velocity = -200 = hex FF38 = [hex FF] [hex 38] = [255] [56] Radius = 500 = hex 01F4 = [hex 01] [hex F4] = [1] [244]

        # 137
        ser.write('\x89')
        time.sleep(.1)
        # 0064 ---> VELOCITY 100
        ser.write('\x00')
        time.sleep(.1)
        # 56
        ser.write('\x64')
        time.sleep(.1)
        # 012C ---> RADIUS 300
        ser.write('\x01')
        time.sleep(.1)
        # 244
        ser.write('\x2C')
        status = 200
    
    if direction == "right-forwards":
    #To drive in reverse at a velocity of -200 mm/s while turning at a radius of 500mm, 
    # #you would send the serial byte sequence [137] [255] [56] [1] [244].
    # Velocity = -200 = hex FF38 = [hex FF] [hex 38] = [255] [56] Radius = 500 = hex 01F4 = [hex 01] [hex F4] = [1] [244]

        # 137
        ser.write('\x89')
        time.sleep(.1)
        # 0064 ---> VELOCITY 100
        ser.write('\x00')
        time.sleep(.1)
        # 56
        ser.write('\x64')
        time.sleep(.1)
        # FED4 ---> RADIUS -300
        ser.write('\xFE')
        time.sleep(.1)
        # 244
        ser.write('\xD4')
        status = 200

    if direction == "right-backwards":
    #To drive in reverse at a velocity of -200 mm/s while turning at a radius of 500mm, 
    # #you would send the serial byte sequence [137] [255] [56] [1] [244].
    # Velocity = -200 = hex FF38 = [hex FF] [hex 38] = [255] [56] Radius = 500 = hex 01F4 = [hex 01] [hex F4] = [1] [244]

        # 137
        ser.write('\x89')
        time.sleep(.1)
        # 0064 ---> VELOCITY 100
        ser.write('\xFF')
        time.sleep(.1)
        # 56
        ser.write('\x9C')
        time.sleep(.1)
        # 012C ---> RADIUS 300
        ser.write('\xFE')
        time.sleep(.1)
        # 244
        ser.write('\xD4')
        status = 200

    if direction == "left-backwards":
    #To drive in reverse at a velocity of -200 mm/s while turning at a radius of 500mm, 
    # #you would send the serial byte sequence [137] [255] [56] [1] [244].
    # Velocity = -200 = hex FF38 = [hex FF] [hex 38] = [255] [56] Radius = 500 = hex 01F4 = [hex 01] [hex F4] = [1] [244]

        # 137
        ser.write('\x89')
        time.sleep(.1)
        # 0064 ---> VELOCITY -100
        ser.write('\xFF')
        time.sleep(.1)
        # 56
        ser.write('\x9C')
        time.sleep(.1)
        # 012C ---> RADIUS 300
        ser.write('\x01')
        time.sleep(.1)
        # 244
        ser.write('\x2C')
        status = 200

    return status



def straight_left(ser):
 #To drive in reverse at a velocity of -200 mm/s while turning at a radius of 500mm, 
    # #you would send the serial byte sequence [137] [255] [56] [1] [244].
    # Velocity = -200 = hex FF38 = [hex FF] [hex 38] = [255] [56] Radius = 500 = hex 01F4 = [hex 01] [hex F4] = [1] [244]

        # 137
        ser.write('\x89')
        time.sleep(.1)
        # 0064 ---> VELOCITY 100
        ser.write('\x00')
        time.sleep(.1)
        # 56
        ser.write('\x64')
        time.sleep(.1)
        # 012C ---> RADIUS 300
        ser.write('\x01')
        time.sleep(.1)
        # 244
        ser.write('\x2C')
        return 200
