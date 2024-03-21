import cv2 as cv

camera = cv.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    modified_to_gray = cv.cvtColor(frame, cv.COLOR_BGR2YCrCb)

    cv.imshow('From camera [0]', modified_to_gray)

    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyAllWindows()
