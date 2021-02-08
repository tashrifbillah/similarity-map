#!/usr/bin/env python

# Author: Tashrif Billah

from draw_box import crop_roi
from sim_map import calc_sim
from find_contours import find_contours
import sys

eta= 0.3

def main():
    
    global eta
    
    # load image, show image, and let draw ROI
    img, roi= crop_roi(sys.argv[1])
       
    # calculate similarity map
    sim_map= calc_sim(img, roi)
    
    # draw contours
    while True:
                
        find_contours(img, sim_map, eta)
        eta= input('Enter a threshold for contour detection [0,1] (q to quit): ')
        
        if eta=='q':
            print('Thank you')
            break
        else:
            eta=float(eta)
        
        

if __name__=='__main__':
    main()
    
    