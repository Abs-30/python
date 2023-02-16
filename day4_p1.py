#%%
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


im= cv.imread("images/GOPR1953.JPG", cv.IMREAD_REDUCED_GRAYSCALE_2)
assert im is not None

w = 3
kernel= np.ones((w,w),np.float32)/(w*w)

im = cv.filter2D(im, -1, kernel)

fig, ax= plt.subplots(1,2, figsize=(10,20))
ax[0].imshow(im, cmap='gray', vmin=0, vmax=255)
ax[0].set_title('Original')
ax[1].imshow(im, cmap='gray', vmin=0, vmax=255)
ax[1].set_title('Average Filtered')
plt.show()
