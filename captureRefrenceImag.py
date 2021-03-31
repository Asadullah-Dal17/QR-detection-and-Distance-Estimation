import cv2 as cv 
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('CaptureRefereImage.mp4', fourcc, 20.0, (640, 480))


camera = cv.VideoCapture(0)
counter =0
while True:
    ret, frame = camera.read()

    cv.imshow("frame", frame)

    out.write(frame)

    key = cv.waitKey(1)
    if key == ord('c'):
        
        print("saved frame")
        cv.imwrite(f"referenceImage{counter}.png", frame)
        counter +=1
    if key == ord('q'):
        break
out.release()
camera.release()
cv.destroyAllWindows()
