def rgb2gray(img):
    
    gray= img[...,0]*0.299+img[...,1]*0.587+img[...,2]*0.114
        
    return gray