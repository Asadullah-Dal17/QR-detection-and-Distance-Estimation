import cv2 as cv
import numpy as np
import math
import pyzbar.pyzbar as pyzbar

# Variable

camID = 0  # camera ID, or pass string as filename. to the camID

# Real world measured Distance and width of QR code
KNOWN_DISTANCE = 24.0  # inches
KNOWN_WIDTH = 5.0  # inches

# define the fonts
fonts = cv.FONT_HERSHEY_COMPLEX

# colors (BGR)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
CYAN = (255, 255, 0)
GOLD = (0, 255, 215)
YELLOW = (0, 255, 255)
ORANGE = (0, 165, 255)

# function

# finding Distance between two points


def eucaldainDistance(x, y, x1, y1):

    eucaldainDist = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)

    return eucaldainDist


def DetectQRcode(image):

    # convert the color image to gray scale image
    Gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # create QR code object
    objectQRcode = pyzbar.decode(Gray)
    for obDecoded in objectQRcode:

        points = obDecoded.polygon
        if len(points) > 4:
            hull = cv.convexHull(
                np.array([points for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points
        n = len(hull)
        for j in range(0, n):
            cv.line(image, hull[j], hull[(j + 1) % n], ORANGE, 2)


# creating camera object
camera = cv.VideoCapture(camID)
# TODO create QR code detector fucntion
# TODO create Eucaldian Distance finder funciton
# TODO focal lenthf finder funciton
# TODO Distance finder funciton

while True:
    ret, frame = camera.read()
    DetectQRcode(frame)
    cv.imshow("frame", frame)

    key = cv.waitKey(1)
    if key == ord('q'):
        break
camera.release()
cv.destroyAllWindows()
