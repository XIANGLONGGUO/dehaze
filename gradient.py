import cv2 as cv
import numpy as np 
#Sobel算子
def sobel_demo(image):
    shape=image.shape
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)   #对x求一阶导
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)   #对y求一阶导
    gradx = cv.convertScaleAbs(grad_x)  #用convertScaleAbs()函数将其转回原来的uint8形式
    grady = cv.convertScaleAbs(grad_y)
    #cv.imshow("gradient_x", gradx)  #x方向上的梯度
    #cv.imshow("gradient_y", grady)  #y方向上的梯度
    #gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0) #图片融合
    gradxy=(gradx**2+grady**2)**0.5
    #cv.imshow("gradient", gradxy)
    gradxy=gradxy.sum()/(shape[0]*shape[1])
    return gradxy
def Scharr_demo(image):
    shape=image.shape
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)   #对x求一阶导
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)   #对y求一阶导
    gradx = cv.convertScaleAbs(grad_x)  #用convertScaleAbs()函数将其转回原来的uint8形式
    grady = cv.convertScaleAbs(grad_y)
    #cv.imshow("gradient_x", gradx)  #x方向上的梯度
    #cv.imshow("gradient_y", grady)  #y方向上的梯度
    #gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    gradxy=(gradx**2+grady**2)**0.5
    gradxy=gradxy.sum()/(shape[0]*shape[1])
    #cv.imshow("gradient", gradxy)
    return gradxy
def Laplace_demo(image):
    shape=image.shape#we can simplify the code by import the size as a constant
    dst = cv.Laplacian(image, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    #cv.imshow("Laplace_demo", lpls)
    lpls=abs(lpls).sum()/(shape[0]*shape[1])
    return lpls
if __name__=="__main__":
    src = cv.imread('./essay/data_img/experiments/1.bmp')
    #cv.namedWindow('input_image', cv.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
    #cv.imshow('input_image', src)
    print(sobel_demo(src))
    print(Scharr_demo(src))
    print(Laplace_demo(src))
    #cv.waitKey(0)

    #cv.destroyAllWindows()
