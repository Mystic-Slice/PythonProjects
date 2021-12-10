import cv2 as cv

path = r"Path\to\Video"
video = cv.VideoCapture(path)
subtractor = cv.createBackgroundSubtractorMOG2(20,50)
while True:

    ret,frame = video.read()

    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Mask',mask)

        if cv.waitKey(5) == ord('x'):
            break

    else:
        video = cv.VideoCapture(path)


cv.destroyAllWindows()
video.release()