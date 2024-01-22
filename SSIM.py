import os 
import torch
import cv2
import numpy as np
from pytorch_msssim import ssim, ms_ssim, SSIM, MS_SSIM
path='./essay/varify/store/img/dark'
ssim_module = SSIM(data_range=1, size_average=True, channel=1)
for i in os.listdir(path):
    #img1=cv2.imread(os.path.join(path,i))
    img1=cv2.imread('./essay/varify/img/2.tif')
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img2=cv2.imread(os.path.join(path,i))
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    print(img1.shape)
    print(img2.shape)
    img1=np.expand_dims(img1,axis=0)
    img2=np.expand_dims(img2,axis=0)
    
    img1=np.expand_dims(img1,axis=0)
    img2=np.expand_dims(img2,axis=0)
    #img2=np.transpose(img2,(0,3,1,2))
    #print(img1)
    #print(img2)

    img1=torch.tensor(img1)/255
    img2=torch.tensor(img2)/255
    #img1=torch.rand((1,1,256,256))
    #img2=torch.rand((1,1,256,256))
    ssim_val = ssim_module(img1, img2)
    print(ssim_val)
