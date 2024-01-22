# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import cv2
import math
import os
def benchmark(stan,path,remove_0=True):
    #load_stan=pd.read_csv(path_stan,sep=',',engine='python',encoding='utf-8')
    load_data=pd.read_csv(path,sep=',',engine='python',encoding='utf-8')
    if load_data.shape[1]==1:
        load_data=pd.read_csv(path,sep='\t',engine='python',encoding='utf-8')
    #if load_stan.shape[1]==1:
        #load_stan=pd.read_csv(path,sep='\t',engine='python',encoding='utf-8')
    
    #print(load_data.shape)
    #print(load_stan.shape)
    #if load_stan.shape!=load_data.shape:
         #raise "ERROR,Shape inequal"
    #else:
         #shape=load_stan.shape
         #print(shape)
    #matrix=load_data-load_stan   
    shape=load_data.shape 
    SUM=0
    SUM2=0
    n=0
    for i in range(shape[0]):
        for j in range(shape[1]):
            #print(load_data.iloc[i,j])
            #print(j)
            if load_data.iloc[i,j] == 0 and remove_0:
                continue
            else:
                n+=1
                SUM+=abs((load_data.iloc[i,j]-stan))
                SUM2+=(load_data.iloc[i,j]-stan)**2
    MAE=SUM/(n)
    MSE=SUM2/(n)
    return SUM , MAE , MSE

if __name__=="__main__":
    path='./essay/varify/displace/dehaze/GCA/mid'
    for i in os.listdir(path):
        if 'csv' in i:
            path1=os.path.join(path,i)
            num_list = [j for j in i if str.isdigit(j)]
            num=int(num_list.pop())
            b,m,s=benchmark(num*.2-0.1,path1)
            print("SUM:{},MAE:{},MSE:{}".format(b,m,s))