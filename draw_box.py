#!/usr/bin/env python

# Author Tashrif Billah
# Reference https://www.geeksforgeeks.org/python-draw-rectangular-shape-and-extract-objects-using-opencv/

import cv2 
import argparse 
  

ref_point = [] 
  
def draw_box(event, x, y, flags, param): 

    global ref_point 
  
    if event == cv2.EVENT_LBUTTONDOWN: 
        ref_point = [(x, y)] 
  
    
    elif event == cv2.EVENT_LBUTTONUP: 
        ref_point.append((x, y)) 
  
        # draw a rectangle around the region of interest 
        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2) 
        cv2.imshow("image", image) 
  
  
image = cv2.imread('img/coins.jpg') 
clone = image.copy() 
cv2.namedWindow("image") 
cv2.setMouseCallback("image", draw_box) 
  
  

while True: 
    cv2.imshow("image", image) 
    key = cv2.waitKey(1) & 0xFF
  
    # press 'r' to reset the window 
    if key == ord("r"): 
        image = clone.copy() 
  
    # press 'q' to break out of the loop
    elif key == ord("q"): 
        break
  
if len(ref_point) == 2: 
    crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]] 
    cv2.imshow("crop_img", crop_img) 
    cv2.waitKey(0) 
    cv2.imwrite('img/cropped.jpg', crop_img)
  

cv2.destroyAllWindows()  
