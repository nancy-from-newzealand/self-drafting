import serial
import time

def forward(ser):
    #To drive in reverse at a velocity of -200 mm/s while turning at a radius of 500mm, 
    # #you would send the serial byte sequence [137] [255] [56] [1] [244].
    # Velocity = -200 = hex FF38 = [hex FF] [hex 38] = [255] [56] Radius = 500 = hex 01F4 = [hex 01] [hex F4] = [1] [244]

    # 137
    ser.write('\x89'.encode())
    time.sleep(.1)
    # 255
    ser.write('\x00'.encode())
    time.sleep(.1)
    # 56
    ser.write('\x64'.encode())
    time.sleep(.1)
    # 1
    ser.write('\x7F'.encode())
    time.sleep(.1)
    # 244
    ser.write('\xFF'.encode())

    return 200

def forward_left(ser):
    #To drive in reverse at a velocity of -200 mm/s while turning at a radius of 500mm, 
    # #you would send the serial byte sequence [137] [255] [56] [1] [244].
    # Velocity = -200 = hex FF38 = [hex FF] [hex 38] = [255] [56] Radius = 500 = hex 01F4 = [hex 01] [hex F4] = [1] [244]

    # 137
    ser.write('\x89'.encode())
    time.sleep(.1)
    # 0064 ---> VELOCITY 100
    ser.write('\x00'.encode())
    time.sleep(.1)
    # 56
    ser.write('\x64'.encode())
    time.sleep(.1)
    # 012C ---> RADIUS 300
    ser.write('\x01'.encode())
    time.sleep(.1)
    # 244
    ser.write('\x2C'.encode())
    return 200

def forward_right(ser):
    #To drive in reverse at a velocity of -200 mm/s while turning at a radius of 500mm, 
    # #you would send the serial byte sequence [137] [255] [56] [1] [244].
    # Velocity = -200 = hex FF38 = [hex FF] [hex 38] = [255] [56] Radius = 500 = hex 01F4 = [hex 01] [hex F4] = [1] [244]

    # 137
    ser.write('\x89'.encode())
    time.sleep(.1)
    # 0064 ---> VELOCITY 100
    ser.write('\x00'.encode())
    time.sleep(.1)
    # 56
    ser.write('\x64'.encode())
    time.sleep(.1)
    # FED4 ---> RADIUS -300
    ser.write('\xFE'.encode())
    time.sleep(.1)
    # 244
    ser.write('\xD4'.encode())

    return 200

def backward(ser):
    #To drive in reverse at a velocity of -200 mm/s while turning at a radius of 500mm, 
    # #you would send the serial byte sequence [137] [255] [56] [1] [244].
    # Velocity = -200 = hex FF38 = [hex FF] [hex 38] = [255] [56] Radius = 500 = hex 01F4 = [hex 01] [hex F4] = [1] [244]

    # 137
    ser.write('\x89'.encode())
    #time.sleep(.1)
    # 255
    ser.write('\xFF'.encode())
    #time.sleep(.1)
    # 56
    ser.write('\x9C'.encode())
    #time.sleep(.1)
    # 1
    ser.write('\x7F'.encode())
    #time.sleep(.1)
    # 244
    ser.write('\xFF'.encode())
    
    return 200

def backward_left(ser):
    #To drive in reverse at a velocity of -200 mm/s while turning at a radius of 500mm, 
    # #you would send the serial byte sequence [137] [255] [56] [1] [244].
    # Velocity = -200 = hex FF38 = [hex FF] [hex 38] = [255] [56] Radius = 500 = hex 01F4 = [hex 01] [hex F4] = [1] [244]

    # 137
    ser.write('\x89'.encode())
    time.sleep(.1)
    # 0064 ---> VELOCITY -100
    ser.write('\xFF'.encode())
    time.sleep(.1)
    # 56
    ser.write('\x9C'.encode())
    time.sleep(.1)
    # 012C ---> RADIUS 300
    ser.write('\x01'.encode())
    time.sleep(.1)
    # 244
    ser.write('\x2C'.encode())

    return 200

def backward_right(ser):
    #To drive in reverse at a velocity of -200 mm/s while turning at a radius of 500mm, 
    # #you would send the serial byte sequence [137] [255] [56] [1] [244].
    # Velocity = -200 = hex FF38 = [hex FF] [hex 38] = [255] [56] Radius = 500 = hex 01F4 = [hex 01] [hex F4] = [1] [244]

    # 137
    ser.write('\x89'.encode())
    time.sleep(.1)
    # 0064 ---> VELOCITY 100
    ser.write('\xFF'.encode())
    time.sleep(.1)
    # 56
    ser.write('\x9C'.encode())
    time.sleep(.1)
    # 012C ---> RADIUS 300
    ser.write('\xFE'.encode())
    time.sleep(.1)
    # 244
    ser.write('\xD4'.encode())

    return 200


def stop(ser):
    #stop: 173 closes all serials
    ser.write('\xAD'.encode())
    return 200


def start_serial():
    # Open a serial connection to Roomba
    ser = serial.Serial(port='/dev/serial0', baudrate=115200)
    return ser

def passive_mode(ser):

    # Assuming the robot is awake, start passive mode. Note that 0x80 in hexadecimal corresponds to 128.
    ser.write('\x80'.encode())
    #time.sleep(.1)
    return 200

def safe_mode(ser):
    # Assuming the robot is awake, start safe mode. Note that 0x82 in hexadecimal corresponds to 130.
    ser.write('\x82'.encode())
    #time.sleep(.1)
    return 200