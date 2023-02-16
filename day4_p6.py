#%%
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

y, x= np.arange(-2, 2.1, 0.1), np.arange(-2, 2.1, 0.1)
Y, X= np.meshgrid(x,y)
sigma = 1000000000000.
g = np.exp(-(X**2+Y**2)/(2*sigma**2))

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, g, cmap=cm.jet, linewidth=0, antialiased=True)
cset = ax.contourf(X, Y, g, zdir='z', offset=np.min(g) -1.5, cmap=cm.jet)
ax.set_zlim(np.min(g) - 2, np.max(g))
plt.axis('off')