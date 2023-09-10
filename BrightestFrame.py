import cv2
import numpy as np

# Open video stream
cap = cv2.VideoCapture(0)  # 0 is the default camera for most systems. Adjust if needed.

def draw_cross(image, center, size, color, thickness):
    """Draw a cross (X) on the image at a specified center."""
    # Define the two lines of the cross based on center and size
    p1 = (int(center[0] - size / 2), int(center[1] - size / 2))
    p2 = (int(center[0] + size / 2), int(center[1] + size / 2))
    p3 = (int(center[0] + size / 2), int(center[1] - size / 2))
    p4 = (int(center[0] - size / 2), int(center[1] + size / 2))

    cv2.line(image, p1, p2, color, thickness)
    cv2.line(image, p3, p4, color, thickness)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find the brightest pixel(s)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

    # Find all pixel coordinates with the same brightness as the brightest pixel
    bright_coords = np.column_stack(np.where(gray == maxVal))

    # Calculate the average position of these pixels
    avg_x = int(np.mean(bright_coords[:, 1]))
    avg_y = int(np.mean(bright_coords[:, 0]))
    avg_pos = (avg_x, avg_y)

    # Draw an 'X' over the average position
    draw_cross(frame, avg_pos, size=30, color=(0, 0, 255), thickness=2)

    # Display the frame
    cv2.imshow('Brightest Pixel', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()
