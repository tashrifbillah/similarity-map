#!/usr/bin/env python

# Author Tashrif Billah
# Reference https://scikit-image.org/docs/dev/auto_examples/edges/plot_contours.html

import matplotlib.pyplot as plt
from matplotlib import image
from skimage import measure
from helpers import rgb2gray

# threshold for contour detection
# Reference https://scikit-image.org/docs/dev/api/skimage.measure.html#find-contours
eta= 0.3

# img= image.imread('img/coins.jpg')
img_rgb= image.imread('img/sim_map.jpg')
# img_rgb= rgb2gray(img)
img_rgb= img_rgb/img_rgb.max()

fig, ax = plt.subplots()
ax.imshow(img_rgb, cmap=plt.cm.gray)

contours = measure.find_contours(img_rgb, eta, fully_connected='high')
for contour in contours:
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)
    
ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
