import numpy as np
import pandas as pd

Data_File_Path='E:\\project\\car\\201904\\dataoutput' #请在这里输入存放day1/2/19/25四个文件夹的路径
ChosenDate='day1' #请在day1/2/19/25中选择
'''
其中这四天的情况分别为
day1:晴天+工作日
day2:雨天+工作日
day19:雨天+周末
day25:晴天+周末
'''

#以下四个是四个路口的转移矩阵，使用dayx_Cross1\2\3\4.csv
transition_matrix_data=[]
for i in range(1,5):
    transition_matrix_data.append(np.array(pd.read_csv(Data_File_Path+'\\'+ChosenDate+'\\'+ChosenDate+'_Cross'+str(i)+'.csv',index_col=0)))


'''
注意在调用时，return的matrix中，如speed_maxtrix(id,epoch)[i,j]，代表从i方向通过id到j方向的车在epoch时间中的平均速度
其中，i,j的取值为0,1,2,3，分别代表西，北，东，南
'''
    

def speed_matrix(id, epoch):
    '''
    TODO 这里直接和kh的模型进行对接，
    注意要加上不同的15分钟时间段，直接写到V里去即可，
    :param:
    id:   "A"/"B"/"C"/"D"
    epoch: 以10s为单位,

    :return:
    4x4 的速度矩阵
    '''
    return


def transition_matrix(id, epoch):
    cross=ord(id)-65 #ABCD通过ASCII读取转为0123
    return transition_matrix_data[cross]


def poisson_matrix(id, epoch):

    pass
