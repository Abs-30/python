import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

im = cv.imread('images/grad.jpg', cv.IMREAD_GRAYSCALE)
assert im is not None

t = np.array([255 - i for i in range(256)], np.uint8)
plt.plot(t)
g = t[im]


cv.namedWindow('image', cv.WINDOW_KEEPRATIO)

cv.imshow('image', im)
cv.waitKey(0)
cv.imshow('image', g)
cv.waitKey(0)

cv.destroyAllWindows()
