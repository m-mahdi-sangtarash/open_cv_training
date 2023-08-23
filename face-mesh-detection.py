import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.FaceMeshModule import FaceMeshDetector


cap = cv2.VideoCapture(1)

face_detector = FaceDetector()
mesh_detector = FaceMeshDetector(maxFaces=2)


while (True):
    rec, frame = cap.read()
    frame, box = face_detector.findFaces(frame)
    frame, faces = mesh_detector.findFaceMesh(frame)

    cv2.imshow('frame', frame)
    exitkey = cv2.waitKey(1) & 0xFF
    if exitkey == 27:
        break

cv2.destroyAllWindows()
cap.release()