import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('Road_in_Norway.jpg')

img_noise_remove = cv2.GaussianBlur(img, (7, 7), 0)

laplacian = cv2.Laplacian(img_noise_remove, cv2.CV_64F)

sobelx = cv2.Sobel(img_noise_remove, cv2.CV_64F, 1, 0, ksize=5)

sobely = cv2.Sobel(img_noise_remove, cv2.CV_64F, 0, 1, ksize=5)

canny = cv2.Canny(img_noise_remove, 100, 300)

plt.subplot(2, 3, 1), plt.imshow(img, cmap='gray')
plt.title('Original')
plt.subplot(2, 3, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian')
plt.subplot(2, 3, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobelx')
plt.subplot(2, 3, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobely')
plt.subplot(2, 3, 5), plt.imshow(canny, cmap='gray')
plt.title('Canny')
plt.show()

