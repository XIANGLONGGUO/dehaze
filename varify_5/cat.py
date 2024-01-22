import pandas as pd
import os
if __name__=="__main__":
    path='./essay/varify/displace'
    init=True
    for i in os.listdir(path):
            print(i)

            if init:
                path1=os.path.join(path,i,'sum.csv')
                df1 = pd.read_csv(path1)
                init=False
            elif init==False:
                path1=os.path.join(path,i,'sum.csv')
                df2 = pd.read_csv(path1)

                # 拼接两个DataFrame，假设它们有相同的行数
                df1 = pd.concat([df1, df2], axis=1)
    df1.to_csv(os.path.join(path,'output.csv'), index=False)