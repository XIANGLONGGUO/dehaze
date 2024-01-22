import numpy as np
from scipy.ndimage import map_coordinates
from scipy.interpolate import interpn, RegularGridInterpolator
#import matplotlib.pyplot as plt
#from PIL import Image
import cv2

def subpixel_translation(image, dx, dy):
    """
    亚像素平移
    """
    
    height, width = image.shape[:2]
    a=np.zeros((height,width,2))
    for i in range(height):
        for j in range(width):
            x=i-dy
            y=j-dx
            a[i,j,1]=y
            a[i][j][0]=x

    x = np.arange(0, width, 1)
    y = np.arange(0, height, 1)
    new_x = np.arange(0, width, 1) + dx
    new_y = np.arange(0, height, 1) + dy
    new_coords = np.column_stack((new_y, new_x))
    #print(new_coords)
    z = image
    z=cv2.cvtColor(z,cv2.COLOR_BGR2GRAY)
    # 双三次插值
    interpolator = RegularGridInterpolator((y, x), z, method='cubic', bounds_error=False, fill_value=0)
    #print(new_coords)


    translated_image = interpolator(a)

    print(translated_image.shape)
    return translated_image.astype(np.uint8)

if __name__ == "__main__":
    path = './essay/varify/Sample7-20/2.tif'
    img = cv2.imread(path)
    print(img.shape)
    from tqdm import tqdm
    for i in tqdm(range(1,11)):
    #dx, dy = 0.5, 0.3  # 亚像素平移的偏移量
        #result = shift_image(img, 0.0, 0.1*i)
        #cv2.imwrite('./essay/varify/img/test_'+str(i)+'.tif',result)
        #input_image = np.array(Image.open("input.jpg"))

    # 缩放图像
        #img = resize(img, 0.5)

    # 亚像素平移

        result = subpixel_translation(img, 0, 0.1*i)
        cv2.imwrite('./essay/varify/img/test_'+str(i)+'.tif',result)

