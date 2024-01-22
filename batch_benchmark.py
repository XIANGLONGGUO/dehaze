from gradient  import Laplace_demo,Scharr_demo,sobel_demo
import cv2
import numpy as np
import os
import glob

def batch_benchmark(work_dir,save_dir,save_name):
    list=os.listdir(work_dir)
    for i in list:
        src = cv2.imread(os.path.join(work_dir,i))
        src=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
        src=src[400:700,410:460]
        sobel=sobel_demo(src)
        scharr=Scharr_demo(src)
        laplace=Laplace_demo(src)
        #print(sobel,scharr,laplace)
        #np.savetxt(os.path.join(save_dir,i[:-4]+'.txt'),np.array([sobel,scharr,laplace]),fmt='%f')
        #if not os.path.exists(os.path.join(save_dir,save_name)):
        #    os.system("touch "+os.path.join(save_dir,save_name))
        with open(os.path.join(save_dir,save_name),"a") as f:
            f.write(i)
            f.write(',')
            f.write(str(sobel))
            f.write(',')
            f.write(str(scharr))
            f.write(',')
            f.write(str(laplace))
            f.write('\n')
if __name__=="__main__":
    work_dir='./essay/data_img/MSRCR'
    save_dir='./essay/grad'
    save_name='result_MSRCR.txt'
    batch_benchmark(work_dir,save_dir,save_name)
            
    