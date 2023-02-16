#%%
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

f = cv.imread ('images/grad.jpg', cv.IMREAD_COLOR)  
assert f is not None

h = np.zeros(256)

h = [np.sum(f==i) for i in range (256)]

plt.bar(range(256), h)
plt.show()


cv.namedWindow ('Image',cv.WINDOW_KEEPRATIO)
cv.imshow ('Image',f)
cv.waitKey (0)
cv.imshow ('Image',g)
cv.waitKey(0)
cv.destroyAllWindows()
