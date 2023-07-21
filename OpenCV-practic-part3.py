import cv2

camra_index = 0
vc = cv2.VideoCapture(camra_index)

weight = vc.get(cv2.CAP_PROP_FRAME_WIDTH)
height = vc.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = vc.get(cv2.CAP_PROP_FPS)

save_path = 'mahdi.avi'
fourcc = cv2.VideoWriter_fourcc(*"XVID")

vw = cv2.VideoWriter(save_path, fourcc, int(fps), (int(weight), int(height)), True)
print("status: ", vc.isOpened())

while vc.isOpened():
    ret, frame = vc.read()
    if not ret:
        print("not working :(")
        break
    cv2.imshow('mahdi', frame)

    vw.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
