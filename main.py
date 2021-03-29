import cv2 as cv
import numpy as np
import math
import pyzbar.pyzbar as pyzbar

# Variable

camID = 1  # camera ID, or pass string as filename. to the camID

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
ORANGE = (0, 165, 230)

# function

# finding Distance between two points


def eucaldainDistance(x, y, x1, y1):

    eucaldainDist = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)

    return eucaldainDist

# focal length finder function


def focalLengthFinder(knowDistance, knownWidth, widthInImage):
    '''This function calculates the focal length. which is used to find the distance between  object and camera 
    :param1 knownDistance(int/float) : it is Distance form object to camera measured in real world.
    :param2 knownWidth(float): it is the real width of object, in real world
    :param3 widthInImage(float): the width of object in the image, it will be in pixels.
    return FocalLength(float): '''
    
    focalLength = ((widthInImage * knowDistance) / knownWidth)
    return focalLength

def distanceFinder(focalLength, knownWidth, widthInImage):
    '''
    This function basically estimate the distance, it takes the three arguments: focallength, knownwidth, widthInImage
    :param1 focalLength: focal length found through another function .
    param2 knownWidth : it is the width of object in the real world.
    param3 width of object: the width of object in the image .
    :returns the distance:


    '''
    distance = ((knownWidth * focalLength) / widthInImage)
    return distance

def DetectQRcode(image):
    codeWidth = 0

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
            print(j, "      ", (j + 1) % n, "    ", n)

            cv.line(image, hull[j], hull[(j + 1) % n], ORANGE, 2)

        x, x1 = hull[0][0], hull[1][0]
        y, y1 = hull[0][1], hull[1][1]
        euclaDistance = eucaldainDistance(x, y, x1, y1)

        return euclaDistance


# creating camera object
camera = cv.VideoCapture(camID)
# TODO create QR code detector fucntion
# TODO create Eucaldian Distance finder funciton
# TODO focal lenthf finder funciton
# TODO Distance finder funciton

while True:
    ret, frame = camera.read()
    codeWidth = DetectQRcode(frame)
    print(codeWidth)

    cv.imshow("frame", frame)

    key = cv.waitKey(1)
    if key == ord('q'):
        break
camera.release()
cv.destroyAllWindows()
