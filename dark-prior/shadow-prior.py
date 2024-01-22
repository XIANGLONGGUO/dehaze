import cv2
import numpy as np


def prepare_image_GRAY(path):#get grad tensor
    img = cv2.imread(path) 
    img = cv2.cvtColor(img, cv2.COLOR_GRAY)
    img= img.astype(np.float32)
    img=np.expand_dims(img,axis=0)
    return img

def prepare_image_RGB(path):#get the tensor after normalized {for torch}
    img = cv2.imread(path) 
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #print(img.shape)
    mean=np.array([0.485,0.456,0.406])
    std=np.array([0.229, 0.224, 0.225])
    img=(img/255-mean)/std
    img=np.transpose(img,(2,0,1))
    img=np.expand_dims(img,axis=0)
    img= img.astype(np.float32)
    return img

def prepare_image_origin(path,CHW=False):#get the img tensor without normalize
    img = cv2.imread(path)
    #img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    if CHW==True:
        img=np.transpose(img,(2,0,1))
    img.astype(np.float32)
    return img

def get_low_pixel(tensor,T_model=False,A=None):#we can get the max of the tensor and the max of channels
    if T_model==True:
        tensor=np.transpose(tensor,(1,2,0))
        tensor=tensor/np.expand_dims(np.expand_dims(A,axis=0),axis=0)
        tensor=np.transpose(tensor,(2,0,1))
    shape=tensor.shape#shape C H W
    low_array=np.zeros(shape[1]*shape[2],dtype=float)
    if len(shape)==2:
        raise "ERROR,we can't get the lowest"
    elif len(shape)==3:
        tensor=tensor.reshape([3,shape[1]*shape[2]])
        l=shape[1]*shape[2]
        for i in range(l):
            B=tensor[0][i]
            G=tensor[1][i]
            R=tensor[2][i]
            low=min([R,G,B])
            low_array[i]=low
        low_array=low_array.reshape([1,shape[1],shape[2]])
        max=np.min(low_array)
        return max,low_array

def get_block(tensor,size,Block=False):#divide the tensor to a list of blocks
    #tensor H W C
    list_tensor=[]
    shape=tensor.shape
    H_fix=size[0]
    W_fix=size[1]
    if Block==False:
        for i in range(shape[0]//H_fix+1):
            a=tensor[i*H_fix:(i+1)*H_fix,:,:]
            a.astype(np.float32)
            if shape[1]%W_fix==0:
                list_tensor.extend(np.split(a,shape[1]//W_fix,axis=1))
            else:
                list_tensor.extend(np.split(a[:,0:W_fix*(shape[1]//W_fix),:],shape[1]//W_fix,axis=1))
                list_tensor.append(a[:,W_fix*(shape[1]//W_fix):shape[1],:]) 
    else:#H,W must %2=1
        
        tensor=np.transpose(tensor,(2,0,1))
        tensor=np.pad(tensor,((0,0),(H_fix//2,H_fix//2),(W_fix//2,W_fix//2)),'constant', constant_values=(255,255))
        tensor=np.transpose(tensor,(1,2,0))
        
        for i in range(shape[0]):
            a=tensor[i:H_fix+i,:,:]
            for k in range(shape[1]):
                list_tensor.append(a[:,k:k+W_fix,:])
    for i in range(len(list_tensor)):
        list_tensor[i].astype(np.float32)
        list_tensor[i]=np.transpose(list_tensor[i],(2,0,1)) 
    return list_tensor,H_fix,W_fix

def method__(path,size):#origin
    img=prepare_image_origin(path)
    shape=img.shape
    list_tensor,H,W=get_block(img,size,True)
    list_A=np.zeros((1,shape[0]*shape[1]))
    n=0
    for i in range((shape[0])*(shape[1])):
        max,_=get_low_pixel(list_tensor[i])
        list_A[0,i]=max
    list_A=list_A.reshape([shape[0],shape[1]])
    return list_A,img
def method_(path,size):
    img=prepare_image_origin(path)
    shape=img.shape
    max,_=get_low_pixel(np.transpose(img,(2,0,1)))
    _=_.reshape([shape[0],shape[1]])
    return _,img

def method(path,size):
    img=prepare_image_origin(path)
    _,t=get_low_pixel(np.transpose(img,(2,0,1)))
    img_F=cv2.erode(t.reshape(img.shape[0],img.shape[1]),np.ones(tuple(size)))
    return img_F,img

def guess_A(img,list_A):
    top_list=[]
    top_pixel=[]
    shape=list_A.shape
    list_A=list_A.reshape([shape[0]*shape[1]])
    print(shape)
    for i in range(int(0.001*(shape[0]*shape[1]))):
        index=list_A.argmax()
        list_A[index]=0
        top_list.append(index)
    for k in top_list:
        #top_pixel.append(img[k//shape[0],k%shape[1]].tolist())
        top_pixel.append(img[k//shape[1]][k%shape[1]].tolist())
    f_=top_pixel[0]
    init_=True
    for j in top_pixel:
        if init_==True:
            fake=np.array([f_])

            init_=False
        else:
            fake=np.append(fake.tolist(),[j],axis=0)
    fake=np.expand_dims(fake,axis=1)
    (w,h,_) = fake.shape
    print(fake.shape)
    img_2D = np.reshape(fake,(-1,3))
    # 统计b,g,r 最大像素的值
    b_max =  np.max(img_2D[:,0])+1
    g_max =  np.max(img_2D[:,1])+1
    r_max =  np.max(img_2D[:,2])+1
    img_tuple = (img_2D[:,0],img_2D[:,1],img_2D[:,2])
    nbin = np.array([b_max,g_max,r_max])
    # 将三维数值 双射 到一个一维数据
    xy = np.ravel_multi_index(img_tuple, nbin) # 0.007s
    # 统计这个数组中每个元素出现的个数
    H = np.bincount(xy, minlength=nbin.prod()) # 0.055s
    H = H.reshape(nbin)
    # 得到最多出现像素的次数
    max_num = H.max() # 0.15s
    # 得到最多出现像素在结果中的像素值
    a = np.unravel_index(np.argmax(H),H.shape)
    return a
        
def get_patch_t(tensor,size,A):
    A=np.expand_dims(np.expand_dims(A,axis=0),axis=0)
    tensor=tensor/A
    _,img=get_low_pixel(np.transpose(tensor,(2,0,1)))
    img_F=cv2.erode(img.reshape(img.shape[1],img.shape[2]),np.ones(tuple(size)))
    #print(img_F)
    return img_F

def get_patch_t_(img,size,A):#original
    shape=img.shape
    list_tensor,H,W=get_block(img,size,True)
    list_A=np.zeros((1,shape[0]*shape[1]))
    n=0
    for i in range((shape[0])*(shape[1])):
        max,_=get_low_pixel(list_tensor[i],True,A)
        list_A[0,i]=max
    list_A=list_A.reshape([shape[0],shape[1]])
    return list_A

def remove(path,size,om=0.95):
    list_A,img=method(path,size)#HWC
    shape=img.shape
    A=guess_A(img,list_A)
    print(A)
   # _,J_dark=get_low_pixel(np.transpose(img,(2,0,1)))
    #_,t_per=get_low_pixel(np.transpose(img,(2,0,1)),True,A)
    t_per=get_patch_t(img,size,A)
    print(t_per.shape)
    New_pic=np.zeros((shape[0],shape[1],3))
    A=np.array(A,dtype=float)
    img.astype(np.float32)
    #t_per.reshape([shape[0]*shape[1]]).tolist()#
    #t_=min(t_per.reshape([shape[0]*shape[1]]).tolist())#
    #img = np.transpose(img,(2,0,1))
    for i in range(shape[0]):
        for j in range(shape[1]):
            t=1-om*t_per[i,j]
            #t=1-om*t_
            #pixels=(img[i,j,:]-np.array([list_A[i,j]]))/max(t,0.1)+np.array([list_A[i,j]])
            pixels=(img[i,j,:]-A)/max(t,0.01)+A
            New_pic[i,j,:]=pixels
    return New_pic

pic=remove("./essay/data_img/",[5,5])

pic.astype(np.uint8)
cv2.imwrite("./a.jpg",pic)

