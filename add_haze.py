import cv2
import numpy as np
def load_img(path):
    img=cv2.imread(path)
    img=img/255
    return img
def add_haze(tensor,t,light):
    img=tensor*t+np.array([[[light*(1-t)]]])
    return img
def main():
    img=load_img('./test_1.jpg')##

    img_haze=add_haze(img,0.03,0.9)

    cv2.imwrite('test_5.jpg',img_haze*255)
if __name__=='__main__':
    main()