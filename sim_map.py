#!/usr/bin/env python

# Author Tashrif Billah
# Reference https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_windowed_histogram.html

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from skimage import data, transform
from skimage.util import img_as_ubyte
from skimage.morphology import disk
from skimage.filters import rank
import cv2

from matplotlib import image
from helpers import rgb2gray

def windowed_histogram_similarity(image, selem, reference_hist, n_bins):
    # Compute normalized windowed histogram feature vector for each pixel
    px_histograms = rank.windowed_histogram(image, selem, n_bins=n_bins)

    # Reshape coin histogram to (1,1,N) for broadcast when we want to use it in
    # arithmetic operations with the windowed histograms from the image
    reference_hist = reference_hist.reshape((1, 1) + reference_hist.shape)

    # Compute Chi squared distance metric: sum((X-Y)^2 / (X+Y));
    # a measure of distance between histograms
    X = px_histograms
    Y = reference_hist

    num = (X - Y) ** 2
    denom = X + Y
    denom[denom == 0] = np.infty
    frac = num / denom

    chi_sqr = 0.5 * np.sum(frac, axis=2)

    # Generate a similarity measure. It needs to be low when distance is high
    # and high when distance is low; taking the reciprocal will do this.
    # Chi squared will always be >= 0, add small value to prevent divide by 0.
    similarity = 1 / (chi_sqr + 1.0e-4)

    return similarity


def calc_sim(img, coin):
    
    if img.shape[-1]==3:
        img= rgb2gray(img)
    img= img.astype('uint8')
    img= img_as_ubyte(img)
    
    if coin.shape[-1]==3:
        coin= rgb2gray(coin)
    coin= coin.astype('uint8')
    coin= img_as_ubyte(coin)

    quantized_img= img // 16
    coin= coin // 16
                         
                         
    # Compute coin histogram and normalize
    coin_hist, _ = np.histogram(coin.flatten(), bins=16, range=(0, 16))
    coin_hist = coin_hist.astype(float) / np.sum(coin_hist)

    # Compute a disk shaped mask that will define the shape of our sliding window
    # A disk with diameter equal to max(w,h) of the roi should be a big enough reference
    selem = disk(max(coin.shape)//2)

    # Compute the similarity across the complete image
    similarity = windowed_histogram_similarity(quantized_img, selem, coin_hist, coin_hist.shape[0])



    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 10))

    axes[0].imshow(quantized_img, cmap='gray')
    axes[0].set_title('Quantized image')
    axes[0].axis('off')
          
    axes[1].imshow(coin, cmap='gray')
    axes[1].set_title('Quantized ROI image')
    axes[1].axis('off')
          
    axes[2].imshow(img, cmap='gray')
    axes[2].imshow(similarity, cmap='hot', alpha=0.5)
    axes[2].set_title('Original image with overlaid similarity')
    axes[2].axis('off')

    plt.tight_layout()
    plt.show(block=False)

    cv2.imwrite('img/sim_map.jpg', similarity)
    
    return similarity

