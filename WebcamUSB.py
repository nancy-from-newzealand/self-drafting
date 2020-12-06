import cv2
 
cap = cv2.VideoCapture(-1)
print(cap)
 
def getImg(display= False,size=[480,240]):
    _, img = cap.read()
    print(img)

    #img = cv2.resize(img,(size[0],size[1]))
    if display:
        cv2.imshow('IMG',img)
    return img, cap
 
if __name__ == '__main__':
    while True:
        img, cap = getImg(True)
        #cap.release()
        