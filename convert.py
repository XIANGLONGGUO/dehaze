import cv2
import numpy as np
import os
def load_img(path):
    img=cv2.imread(path)
    
    return img
def write_img(name,tensor):
    tensor=cv2.cvtColor(tensor,cv2.COLOR_RGB2GRAY)
    cv2.imwrite(name,tensor)
path='./essay/varify/selected'
path1='./essay/varify/selected'
for i in os.listdir(path):
    img=load_img(os.path.join(path,i))
    print(img.shape)
    img=img[:,:800]
    print(img.shape)
    write_img(os.path.join(path1,i),img)