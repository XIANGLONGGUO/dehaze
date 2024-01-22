import cv2
import numpy as np
import matplotlib.pyplot as plt
def move(path,name,dx,dy):
    img = cv2.imread(path)  # 读取彩色图像(BGR)
    rows, cols, ch = img.shape

    MAT = np.float32([[1, 0, dx], [0, 1, dy]])  # 构造平移变换矩阵   
    dst = cv2.warpAffine(img, MAT, (cols, rows),flags=cv2.INTER_LINEAR)  # 默认为黑色填充
    cv2.imwrite(name,dst)
import cv2
import numpy as np
import matplotlib.pyplot as plt

def bilinear_interpolation(img, x, y):
    x0, y0 = int(x), int(y)
    x1, y1 = x0 + 1, y0 + 1

    if x1 >= img.shape[1]:
        x1 = x0
    if y1 >= img.shape[0]:
        y1 = y0

    # 计算权重
    dx, dy = x - x0, y - y0
    w00 = (1 - dx) * (1 - dy)
    w01 = dx * (1 - dy)
    w10 = (1 - dx) * dy
    w11 = dx * dy

    # 使用双线性插值计算新像素值
    interpolated_value = w00 * img[y0, x0] + w01 * img[y0, x1] + w10 * img[y1, x0] + w11 * img[y1, x1]

    return interpolated_value

def shift_image(img, dx, dy):
    rows, cols, _ = img.shape
    result = np.zeros_like(img)

    for y in range(rows):
        for x in range(cols):
            new_x, new_y = x - dx, y - dy
            if 0 <= new_x < cols and 0 <= new_y < rows:
                result[y, x] = bilinear_interpolation(img, new_x, new_y)

    return result

if __name__ == "__main__":
    path = './essay/varify/img/2.jpg'
    img = cv2.imread(path)
    from tqdm import tqdm
    for i in tqdm(range(1,11)):
    #dx, dy = 0.5, 0.3  # 亚像素平移的偏移量
        result = shift_image(img, 0, 0.1*i)
        cv2.imwrite('./essay/varify/img/test_'+str(i)+'.tif',result)



##a