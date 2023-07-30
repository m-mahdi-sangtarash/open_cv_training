import cv2

camera_index = 1
vc = cv2.VideoCapture(camera_index)

width = vc.get(cv2.CAP_PROP_FRAME_WIDTH)
height = vc.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = vc.get(cv2.CAP_PROP_FPS)

save_path = 'mahdi-opencv.avi'
fourcc = cv2.VideoWriter_fourcc(*"XVID")

vw = cv2.VideoWriter(save_path, fourcc, int(fps), (int(width), int(height)), True)

detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


print("Status: ", vc.isOpened())

while vc.isOpened():
    ret, frame = vc.read()
    if not ret:
        print("not working :(")
        break
    boxes = detector.detectMultiScale(frame)
    for box in boxes:
        x1, y1, width, height = box
        x2, y2 = x1 + width, y1 + height
        cv2.rectangle(frame, (x1,y1), (x2, y2), (0,255,0))
        cv2.putText(frame, 'Face', (x1, y1), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255))
    cv2.imshow('mahdi-opncv', frame)
    vw.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

