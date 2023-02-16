#%%
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

f = cv.imread('images/grad.jpg', cv.IMREAD_GRAYSCALE)
assert f is not None

g = cv.equalizeHist(f)

fig, ax = plt.subplots(1,2, figsize=(12,24))
ax[0].imshow(f, cmap='gray', vmin=0, vmax=255)
ax[1].imshow(g, cmap='gray', vmin=0, vmax=255)
plt.show()
