import cv2 as cv
# colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
CYAN = (255, 255, 0)
GOLD = (0, 255, 215)
YELLOW = (0, 255, 255)
ORANGE = (0, 165, 230)


def showText(image, text, position,  color, animateOnValue=None):
    fonts = cv.FONT_HERSHEY_COMPLEX
    x, y = position
    # move the callout up little bit.
    y = y - 20
    # how much tick line should be, 
    lineThicknes = 30
    offset = int(lineThicknes / 2)
    center = int(offset / 2)
    new_pos = (x, y + center)
    lineLength = 229

    newThickness = int(lineThicknes * 0.7)
    
    cv.line(image, (x, y), (x+lineLength, y), ORANGE, lineThicknes)
    cv.line(image, (x, y), (x+lineLength, y), GREEN, newThickness)
    if animateOnValue is not None:

        cv.line(image, (x, y), (x+animateOnValue, y), WHITE, newThickness)
    # cv.line(image, (x,y-11), (x+Distance_level, y-11), (GREEN), 18)
    cv.putText(image, text, new_pos, fonts, 0.6, BLACK, 2)

