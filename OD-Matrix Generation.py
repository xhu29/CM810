#This work was jointly done by Xi Hu and Shuai Hao.

import pandas as pd
import numpy as np
import datetime
from datetime import datetime as ti
import os, random, shutil

def timechange(time):
    # Change the format of the time
    t=datetime.datetime.strptime(time,"%m/%d/%Y %H:%M")
    t=ti.fromisoformat(str(t)).timestamp()
    return t

def od(time_1,time_2,corpus,n):
    # input: data, time_start, time_end and data number
    # output: one matric which contains the data from time_start to time_end
    a=[]
    b=[]
    for i in range(len(corpus)):
        time=timechange(corpus[i][0])
        if time < time_2 and time >= time_1:
            a.append(corpus[i][2])
            b.append(corpus[i][3])
   
    
    s=np.zeros((77, 77)) #"77" is the greatest value that represents the community area.
    for i in range(len(a)):
        x=a[i]-1
        y=b[i]-1
        s[x][y]+=1
    return s


#Load the data
corpus = pd.read_csv('Data.csv')
corpus = corpus.values.tolist()
print(type(corpus))

#Set up time_start and time_end
time_start='1/1/2020 00:00'
time_end='1/31/2020 13:15'
time_1=timechange(time_start)
time_2=timechange(time_end) 

n=1
while time_1< time_2:
    time_3=time_1 + 6*3600
    k= od(time_1,time_3,corpus,n)
    np.savetxt(str(n) + '.csv', k, delimiter=",")
    time_1=time_3
    n+=1
    
def moveFile(fileDir，tarDir):
    # randomly pick up some samples as train,test and validation.
    # input: fileDir---the original data folder, tarDir----the train,test and validation folder
    pathDir = os.listdir(fileDir)    
    filenumber=len(pathDir)
    rate=0.1    
    picknumber=int(filenumber*rate) 
    sample = random.sample(pathDir, picknumber)  
    print (sample)
    for name in sample:
        shutil.move(fileDir+name, tarDir+name)
    return
    
fileDir="OD Matrix./data/"
tarDir="Sampling OD Matrix./training/"
moveFile(fileDir，tarDir)
