#%%
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


im= cv.imread("images/20210212-YearoftheOx_EN-US5106152536_UHD.jpg", cv.IMREAD_REDUCED_GRAYSCALE_2)
assert im is not None

blurred = cv.blur(im,(11,11))
hp = cv.subtract(im, blurred)
sharpened = cv.addWeighted(im,1.0,hp,1.5,0)



fig, ax= plt.subplots(1,4, figsize=(20,40))
ax[0].imshow(im, cmap='gray', vmin=0, vmax=255)
ax[0].set_title('Original')
ax[1].imshow(blurred, cmap='gray', vmin=0, vmax=255)
ax[1].set_title('Blurred')
ax[2].imshow(hp, cmap='gray', vmin=0, vmax=255)
ax[2].set_title('High Contrast')
ax[3].imshow(sharpened, cmap='gray', vmin=0, vmax=255)
ax[3].set_title('Sharpened')
plt.show()