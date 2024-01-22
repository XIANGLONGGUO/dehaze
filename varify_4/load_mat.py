import scipy.io
import os
mode='b1'
path=os.path.join('./essay/varify/mat/'+mode+'.mat')
path1='./essay/varify/displace'
# 读取.mat文件
import hdf5storage
import os 
import pandas as pd
data = hdf5storage.loadmat(path)

# 获取.mat文件中的变量
variable = data['data_dic_save']

dis=variable['displacements']
dis_v=dis['plot_v_dic']
print(len(dis_v[0][0][0]))
# 打印变量
if os.path.exists(os.path.join(path1,mode))==False:
    os.mkdir(os.path.join(path1,mode))
for i in range(1,11):
    #print(dis_v)
    df = pd.DataFrame(dis_v[0][0][i-1])

    # Writing the DataFrame to a CSV file
    df.to_csv(os.path.join(path1,mode,str(i)+'.csv'), index=False)