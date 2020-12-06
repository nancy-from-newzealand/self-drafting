import cv2
 
cap = cv2.VideoCapture(-1)
#cap.release()
print(cap)
 
def getImg(display= False,size=[480,240]):
    _, img = cap.read()
    print(img)

    img = cv2.resize(img,(size[0],size[1]))
    if display:
        cv2.imshow('IMG',img)
        # cv2.waitKey()
    return img, cap
 
if __name__ == '__main__':
    while True:
        img, cap = getImg(True)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
        