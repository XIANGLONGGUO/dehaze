import scipy.io
import os

mod='Sample7'


for j in os.listdir(os.path.join('./essay/varify/mat',mod)):
    mode=os.path.splitext(j)[0]
    path=os.path.join(os.path.join('./essay/varify/mat',mod),mode+'.mat')
    path1='./essay/varify/displace'+mod
    if os.path.exists(path1)==False:
        os.mkdir(path1)
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
    for i in range(0,11):###十张用1，11
        #print(dis_v)
        df = pd.DataFrame(dis_v[0][0][i])###十张用i-1

        # Writing the DataFrame to a CSV file
        df.to_csv(os.path.join(path1,mode,str(i)+'.csv'), index=False)