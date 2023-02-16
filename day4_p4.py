#%%
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


im= cv.imread("images/GOPR1953.JPG", cv.IMREAD_REDUCED_GRAYSCALE_2)
assert im is not None


sobel_h= np.array([[-1,0,1],[-2,0,2],[-1,0,1]], np.float32)
imh = cv.filter2D(im.astype('float'), -1, sobel_h)
imh = cv.normalize(imh.astype('float'), None,0, 255.0, cv.NORM_MINMAX)

sobel_v= np.array([[-1,-2,-1],[0,0,0],[1,2,1]], np.float32)
imv = cv.filter2D(im.astype('float'), -1, sobel_v)
imv = cv.normalize(imv.astype('float'), None,0, 255.0, cv.NORM_MINMAX)

fig, ax= plt.subplots(1,3, figsize=(10,20))
ax[0].imshow(im, cmap='gray', vmin=0, vmax=255)
ax[0].set_title('Original')
ax[1].imshow(imh, cmap='gray', vmin=0, vmax=255)
ax[1].set_title('Sobel Horizontal Filtered')
ax[2].imshow(imv, cmap='gray', vmin=0, vmax=255)
ax[2].set_title('Sobel Vertical Filtered')
plt.show()