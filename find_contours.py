#!/usr/bin/env python

# Author Tashrif Billah
# Reference https://scikit-image.org/docs/dev/auto_examples/edges/plot_contours.html

import matplotlib.pyplot as plt
from matplotlib import image
from skimage import measure
from helpers import rgb2gray

# threshold for contour detection
# Reference https://scikit-image.org/docs/dev/api/skimage.measure.html#find-contours

def find_contours(img, sim_map, eta):
    
    sim_map= sim_map/sim_map.max()
    
    fig, ax = plt.subplots()
    ax.imshow(img, cmap='gray')
    ax.imshow(sim_map, cmap='hot', alpha=0.5)

    contours = measure.find_contours(sim_map, eta, fully_connected='high')
    for contour in contours:
        ax.plot(contour[:, 1], contour[:, 0], linewidth=2)
        
    ax.axis('image')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f'Contours for eta={eta}')
    plt.show(block=False)
