import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(imgray, 12, 255, cv2.THRESH_BINARY)
ret2, threshold2 = cv2.threshold(imgray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

threshold3 = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 1)


cv2.imshow('threshold', threshold3)
cv2.waitKey(0)
