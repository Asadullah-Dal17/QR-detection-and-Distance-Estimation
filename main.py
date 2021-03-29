import cv2 as cv
import numpy as np

camID = 1

camera = cv.VideoCapture(camID)
# TODO create QR code detector fucntion
# TODO create Eucaldian Distance finder funciton
# TODO focal lenthf finder funciton
# TODO Distance finder funciton

while True:
    ret, frame = camera.read()
    cv.imshow("frame", frame)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
camera.release()
cv.destroyAllWindows()
