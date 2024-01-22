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
    Sum3=0
    Sum4=0
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
                Sum3+=load_data.iloc[i,j]
                Sum4+=load_data.iloc[i,j]**2
    MAE=SUM/(n)
    MSE=SUM2/(n)
    Mean=Sum3/(n)
    Var=Sum4/(n)-Mean**2
    return SUM , MAE , MSE, Mean, Var

if __name__=="__main__":
    for j in os.listdir('./essay/varify/displace'):
        path_0='./essay/varify/displace'
        mode=j
        path=os.path.join(path_0,mode)
        n=0
        print(j)
        dict={}
        for i in os.listdir(path):
            if 'csv' in i and [j for j in i if str.isdigit(j)]!=[]:
                path1=os.path.join(path,i)
                num_list = [j for j in i if str.isdigit(j)]
                num_list=''.join(num_list)
                num=int(num_list)
                #print(num)
                b,m,s,a,v=benchmark(num*.1,path1)
                dict[num]=(b,m,s,a,v,num*0.1-a)
                print(i)
                print("SUM:{},MAE:{},MSE:{},MEAN:{},Var:{},Loss:{}".format(b,m,s,a,v,num*0.1-a))
                n+=1
                if n==1:
                    with open(os.path.join(path,'sum.csv'),'w') as f:
                        f.write('num '+mode)
                        f.write(',')
                        f.write('SUM '+mode)
                        f.write(',')
                        f.write('MAE '+mode)
                        f.write(',')
                        f.write('MSE '+mode)
                        f.write(',')
                        f.write('MEAN '+mode)
                        f.write(',')
                        f.write('Var '+mode)
                        f.write(',')
                        f.write('Loss '+mode)
                        f.write('\n')
        for i in range(0,11):
                with open(os.path.join(path,'sum.csv'),'a') as f:
                    b,m,s,a,v,l=dict[i]
                    f.write(str(format(i*0.1,'.4g')))
                    f.write(',')
                    f.write(str(b))
                    f.write(',')
                    f.write(str(m))
                    f.write(',')
                    f.write(str(s))
                    f.write(',')
                    f.write(str(a))
                    f.write(',')
                    f.write(str(v))
                    f.write(',')
                    f.write(str(l))
                    f.write('\n')

        