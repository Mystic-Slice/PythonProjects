import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

while True:
    ret,frame = camera.read()

    cv.imshow('Camera',frame)

    # grainy output
    laplacian = cv.Laplacian(frame,cv.CV_64F)
    laplacian = np.uint8(laplacian)
    cv.imshow('Laplacian',laplacian)
    # Only outline in output
    edges = cv.Canny(frame,125,125)
    cv.imshow('Canny',edges)

    if cv.waitKey(5) == ord('x'):
        break

camera.release()
cv.destroyAllWindows()