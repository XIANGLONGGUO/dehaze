import cv2
import numpy as np
import os
def load_img(path):
    img=cv2.imread(path)
    img=img/255
    return img
def add_haze(tensor,t,light):
    if len(tensor.shape)==3:
        img=tensor*t+np.array([[[light*(1-t)]]])
    else:
        img=tensor*t+np.array([[light*(1-t)]])
    return img
def main():
    path='./essay/varify/haze/mid'
    path1='./essay/varify/haze'
    for i in os.listdir(path):
        img=load_img(os.path.join(path,i))
        img=add_haze(img,0.3,0.7)
        cv2.imwrite(os.path.join(path1,'b1',os.path.splitext(i)[0] + '.bmp'),img*255)
if __name__=='__main__':
    main()