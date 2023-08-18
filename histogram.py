import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img-histogram.jpg', 0)
img_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
equalized_hist = cv2.equalizeHist(img)
img_equalize_hist = cv2.calcHist([equalized_hist], [0], None, [256], [0, 256])

clache = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clache.apply(img)
cl1_equalize_hist = cv2.calcHist([cl1], [0], None, [256], [0, 256])

plt.subplot(3, 2, 1), plt.imshow(img, 'gray')
plt.subplot(3, 2, 2), plt.plot(img_hist, 'gray')
plt.subplot(3, 2, 3), plt.imshow(equalized_hist, 'gray')
plt.subplot(3, 2, 4), plt.plot(img_equalize_hist, 'gray')
plt.subplot(3, 2, 5), plt.imshow(cl1, 'gray')
plt.subplot(3, 2, 6), plt.plot(cl1_equalize_hist, 'gray')
plt.show()

