import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1)

detector = HandDetector(detectionCon= 0.5, maxHands=2)

while (True):
    rec, frame = cap.read()
    hand, image = detector.findHands(frame)
    cv2.imshow('frame', frame)
    exitkey = cv2.waitKey(1) & 0xFF
    if exitkey == 27:
        break

cv2.destroyAllWindows()
cap.release()