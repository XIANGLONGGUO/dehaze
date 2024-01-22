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
    sets='img2'
    path=os.path.join('./essay/varify',sets)
    path1='./essay/varify/haze'
    mode='global'
    path1=os.path.join(path1,sets)

    if os.path.exists(path1)==False:
        os.mkdir(path1)
    mode='global'
    if os.path.exists(os.path.join(path1,mode))==False:
        os.mkdir(os.path.join(path1,mode))
    for i in os.listdir(path):
        img=load_img(os.path.join(path,i))
        img=add_haze(img,0.5,0.5)
        cv2.imwrite(os.path.join(path1,mode,os.path.splitext(i)[0] + '.bmp'),img*255)
if __name__=='__main__':
    main()