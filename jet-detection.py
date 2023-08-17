import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('jets.jpg', 0)

template = cv2.imread('jet-temp.jpg', 0)

width, height = template.shape

result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

threshold = 0.8

location = np.where(result >= threshold)

for points in zip(*location[::-1]):
    cv2.rectangle(img, points, (points[0] + height, points[1] + width), (255, 255, 0), 2)


plt.imshow(img)
plt.show()