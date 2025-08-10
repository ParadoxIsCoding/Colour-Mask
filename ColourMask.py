import cv2
import numpy as np


def process_frame(frame):
    # Convert the image from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range for the color orange
    # Note: You may need to adjust these values based on your specific shade of orange
    lower_orange = np.array([5, 50, 50])
    upper_orange = np.array([15, 255, 255])

    # Create a binary mask where the pixels within the orange range are set to 255 and everything else is set to 0
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    return mask
# Test Commit 3

def live_orange_mask():
    # Open the video capture stream
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Couldn't open the camera.")
        return

    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()

        if not ret:
            print("Error: Couldn't read a frame.")
            break

        # Process the frame
        mask = process_frame(frame)

        # Display the mask
        cv2.imshow('Orange Mask Live Feed', mask)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture stream and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


# Start the live video feed processing
live_orange_mask()
