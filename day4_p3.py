#%%
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


im= cv.imread("images/GOPR1953.JPG", cv.IMREAD_REDUCED_GRAYSCALE_2)
assert im is not None


sobel_h= np.array([[-1,0,1],[-2,0,2],[-1,0,1]], np.float32)

imh = cv.filter2D(im.astype('float'), -1, sobel_h)

imh = cv.normalize(imh.astype('float'), None,0, 255.0, cv.NORM_MINMAX)

fig, ax= plt.subplots(1,2, figsize=(10,20))
ax[0].imshow(im, cmap='gray', vmin=0, vmax=255)
ax[0].set_title('Original')
ax[1].imshow(imh, cmap='gray', vmin=0, vmax=255)
ax[1].set_title('Sobel Horizontal Filtered')
plt.show()