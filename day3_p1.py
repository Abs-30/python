import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

f = cv.imread ('images/grad.jpg', cv.IMREAD_GRAYSCALE)
assert f is not None

t = np.arange(0,256).astype(np.uint8)
t[0:99] = 0
t[201:255] = 0
plt.plot(t)
g=t[f]


