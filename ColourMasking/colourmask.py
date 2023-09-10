import cv2
import numpy as np
################
image = cv2.imread("images/cone.png")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
################

colourDict={
    "numbers":[(15,50,180),(40,255,255)],
    "cone":[(174,59,50),(179,255,255)]
}

desiredMask = input("\n\nWhat do you want to mask for?\n= ")
lower_colour = colourDict[desiredMask][0]
upper_colour = colourDict[desiredMask][1]
###############
mask = cv2.inRange(hsv, lower_colour, upper_colour)
result = cv2.bitwise_and(image, image, mask=mask)
###############
cv2.imshow("Mask",mask)
cv2.waitKey(0)
cv2.imshow("Masked Image",result)
cv2.waitKey(0)
cv2.destroyAllWindows()