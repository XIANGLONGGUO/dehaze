import cv2
import numpy as np
def load_img(path):
    img=cv2.imread(path)
    
    return img
def write_img(name,tensor):
    cv2.imwrite(name,tensor)
img=load_img('./test_5.png')
print(img.shape)
#img=img[0:500]
print(img.shape)
write_img('./test_5.tif',img)