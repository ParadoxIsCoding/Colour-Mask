import cv2
import numpy as np
import time
################
colourDict={
    "numbers":[(15,50,180),(40,255,255)],
    "cone":[(174,59,50),(179,255,255)]
}

desiredMask = input("\n\nWhat do you want to mask for?\n= ")
lower_colour = colourDict[desiredMask][0]
upper_colour = colourDict[desiredMask][1]
################
#image = cv2.imread("images/cone.png")

def maskFrame(_frame):
    hsv = cv2.cvtColor(_frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_colour, upper_colour)
    result = cv2.bitwise_and(_frame, _frame, mask=mask)
    return mask, result
################
def run():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened: 
        print("Error opening camera, press any key to quit")
        cv2.waitKey(0)
        quit()

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error: couldn't read a frame, press any key to quit")
            cv2.waitKey(0)
            quit()
        mask, result = maskFrame(frame)
        cv2.imshow("Mask", mask)
        cv2.imshow("Masked Image", result)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()
run()