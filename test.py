import cv2
import serial

ser = serial.Serial(port='/dev/serial0', baudrate=115200)
ser.close()

# cap = cv2.VideoCapture(-1)
# cap.release()
# print(cap)