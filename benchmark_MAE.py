import pandas as pd
import numpy as np
import cv2
import math

def benchmark(path_stan,path,remove_0=True):
    load_stan=pd.read_csv(path_stan,sep=',',engine='python',encoding='utf-8')
    load_data=pd.read_csv(path,sep=',',engine='python',encoding='utf-8')
    if load_data.shape[1]==1:
        load_data=pd.read_csv(path,sep='\t',engine='python',encoding='utf-8')
    if load_stan.shape[1]==1:
        load_stan=pd.read_csv(path,sep='\t',engine='python',encoding='utf-8')
    
    print(load_data.shape)
    print(load_stan.shape)
    if load_stan.shape!=load_data.shape:
         raise "ERROR,Shape inequal"
    else:
         shape=load_stan.shape
         #print(shape)
    #matrix=load_data-load_stan    
    SUM=0
    SUM2=0
    n=0
    for i in range(shape[0]):
        for j in range(shape[1]):
            #print(load_data.iloc[i,j])
            #print(j)
            if load_data.iloc[i,j] == 0 and load_stan.iloc[i,j]==0 and remove_0:
                continue
            else:
                SUM+=abs((load_data.iloc[i,j]-load_stan.iloc[i,j]))
                SUM2+=(load_data.iloc[i,j]-load_stan.iloc[i,j])**2
    MAE=SUM/(shape[1]*shape[0])
    MSE=SUM2/(shape[1]*shape[0])
    return SUM , MAE , MSE

if __name__=="__main__":
    path='./essay/data_csv/origin.csv'
    path1='./essay/data_csv/origin_haze.csv'
    b,m,s=benchmark(path,path1)
    print("SUM:{},MAE:{},MSE:{}".format(b,m,s))