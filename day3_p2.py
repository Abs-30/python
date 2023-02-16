#%%
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

f = cv.imread ('images/grad.jpg', cv.IMREAD_COLOR)
assert f is not None

gamma = 0.5
t = np.array([(i/255.)**gamma*255 for i in range (256)], np.uint8)
g = t[f]

# %%
plt.plot(t)
plt.show()

#%%
cv.namedWindow ('Image',cv.WINDOW_KEEPRATIO)
cv.imshow ('Image',f)
cv.waitKey (0)
cv.imshow ('Image',g)
cv.waitKey(0)



cv.destroyAllWindows()