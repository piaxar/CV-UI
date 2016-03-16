import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if __name__ == '__main__':
    while (True):
        ret, frame = cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #
        edges = cv2.Canny(img, 100, 100)
        cv2.imshow("Canny", edges)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows
