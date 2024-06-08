import cv2 as cv
import os


root = "./Videos"
files = os.listdir(root)
video_lst = [f for f in files if f.endswith('.mp4') and os.path.isfile(os.path.join(root, f))]

print(files)
i = 0
image_num = 1
while i < len(video_lst):
    video_name = video_lst[i]
    video = f"./Videos/{video_name}"
    cap = cv.VideoCapture(video)

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % 45 == 0:
            cv.imwrite(f'./frames/image-{image_num}.jpg', frame)
            image_num += 1
        print(frame_count)
        frame_count += 1

    i += 1
    cv.destroyAllWindows()