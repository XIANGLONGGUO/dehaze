import os 
import cv2
import numpy as np
import pandas as pd
import numpy.linalg as la
def distance(x,y):
    return la.norm(x-y)
def sobel_demo(image):
    shape=image.shape
    grad_x = cv2.Sobel(image, cv2.CV_32F, 1, 0)   #对x求一阶导
    grad_y = cv2.Sobel(image, cv2.CV_32F, 0, 1)   #对y求一阶导
    gradx = cv2.convertScaleAbs(grad_x)  #用convertScaleAbs()函数将其转回原来的uint8形式
    grady = cv2.convertScaleAbs(grad_y)
    grad=np.sqrt(gradx**2+grady**2)
    return grad
'''def guess_mid(image,window_size=15):
    shape=image.shape
    mid=np.zeros(shape)
    '''
def dehaze(img_refer,img_corr,windows_size=15):##for gray image
    if img_refer.shape != img_corr.shape:
        raise ValueError('img_refer.shape != img_corr.shape')
    '''shape=img_refer.shape
    mid=(shape[0]//2,shape[1]//2)
    low_index=np.argmin(img_refer)
    low_index=(low_index//shape[1],low_index%shape[1])
    low_refer=img_refer[low_index]
    low_block=img_corr[low_index[0]-windows_size:low_index[0]+windows_size,low_index[1]-windows_size:low_index[1]+windows_size]
    low_corr=cv2.erode(low_block,np.ones((windows_size,windows_size)))
    low_corr=np.min(low_corr)
    '''
    shape=img_refer.shape
    low_refer=cv2.erode(img_refer,np.ones((windows_size,windows_size)))
    low_corr=cv2.erode(img_corr,np.ones((windows_size,windows_size)))
    high_refer=cv2.dilate(img_refer,np.ones((windows_size,windows_size)))
    high_corr=cv2.dilate(img_corr,np.ones((windows_size,windows_size)))

    t=np.zeros(shape)
    A=np.zeros(shape)


    for i in range(shape[0]):
        for j in range(shape[1]):
            t[i,j]=min(abs((high_corr[i,j]-low_corr[i,j])/(high_refer[i,j]-low_refer[i,j])),0.99)   
            t[i,j]=max(t[i,j],0.01)    
            A[i,j]=((high_corr[i,j]-t[i,j]*high_refer[i,j])/(1-t[i,j])+(low_corr[i,j]-t[i,j]*low_refer[i,j])/(1-t[i,j]))/2

    dehaze_img=(img_corr-A*(1-t))/(t) 
    return dehaze_img       
if __name__=='__main__':
    refer='./essay/varify/Sample7/2.tif'
    dir="./essay/varify/haze/mid"
    #refer='./essay/varify/ex/2.tiff'
    #dir="./essay/varify/ex"
    s_dir="./essay/varify/dehaze/my_e"
    img1=cv2.imread(refer)
    img1=cv2.cvtColor(img1,cv2.COLOR_RGB2GRAY)
    if os.path.exists(s_dir)==False:
        os.makedirs(s_dir)
    list=os.listdir(dir)
    n=0
    for i in list:
        j=os.path.join(dir,i)
        img2=cv2.imread(j)
        img2=cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
        pic=dehaze(img1,img2,21)
        
        pic=pic.astype(np.uint8)
        #print(os.path.join(s_dir,i))

        cv2.imwrite(os.path.join(s_dir,i),pic)
        n+=1