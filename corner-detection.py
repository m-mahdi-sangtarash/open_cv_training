import cv2
import matplotlib.pyplot as plt


img = cv2.imread('hello-world.jpg')
img_g = cv2.imread('hello-world.jpg', 0)

corner_det = cv2.cornerHarris(img_g, 3, 7, 0.14)
corner_dilate = cv2.dilate(corner_det, None)
img[corner_dilate > 0.01 * corner_dilate.max()] = [255, 0, 0]

plt.imshow(img)
plt.show()