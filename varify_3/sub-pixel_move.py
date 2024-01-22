import cv2
import numpy as np
import matplotlib.pyplot as plt
def move(path,name,dx,dy):
    img = cv2.imread(path)  # 读取彩色图像(BGR)
    rows, cols, ch = img.shape

    MAT = np.float32([[1, 0, dx], [0, 1, dy]])  # 构造平移变换矩阵   
    dst = cv2.warpAffine(img, MAT, (cols, rows),flags=cv2.INTER_LINEAR)  # 默认为黑色填充
    cv2.imwrite(name,dst)
if __name__=="__main__":
    path='./essay/varify_2/img/2.jpg'
    for i in range(1,21):
        move(path,'./essay/varify_2/img/test_'+str(i)+'.jpg',0,i*0.05)
