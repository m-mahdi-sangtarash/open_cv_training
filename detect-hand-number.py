import cv2 as cv
from cvzone.HandTrackingModule import HandDetector


cap = cv.VideoCapture(1)

hand_detector = HandDetector(detectionCon=0.8, maxHands=2)
fingers_up = 0

while (True):
    _, frame =cap.read()
    hand, _ = hand_detector.findHands(frame)
    if hand:
        hand = hand[0]
        fingers = hand_detector.fingersUp(hand)
        for i in fingers:
            if i == 1:
                fingers_up += 1
        cv.putText(frame, f"{fingers_up}",(50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
        print(fingers)
    cv.imshow('frame', frame)
    fingers_up = 0
    exit_key = cv.waitKey(1) & 0xFF

    if exit_key == 27:
        break
cv.destroyAllWindows()
cap.release()