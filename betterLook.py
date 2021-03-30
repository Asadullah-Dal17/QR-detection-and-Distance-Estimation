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

def showText(image, text, position,  color):
    fonts = cv.FONT_HERSHEY_COMPLEX
    x, y =position
    cv.line(image, (x, y-9), (x+180, y-9), MAGENTA, 20)
    # cv.line(image, (x,y-11), (x+Distance_level, y-11), (GREEN), 18)
    
    cv.putText(image, text, position, fonts, 0.5, color, 2)




