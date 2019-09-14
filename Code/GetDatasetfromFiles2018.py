import os
import re
import sys
import numpy as np
from collections import Counter
import collections
import h5py
import pandas as pd

p=os.path.abspath('C:\\Users\\Vicky\\Desktop\\Courses\\Avi\\erisk collections_2017_2018\\erisk collections\\2017\\2test')
os.chdir(p)

#############Read Output ###############################################
y_train = pd.read_excel('y_train.xlsx', sheetname='sheet1')

############# Read First Dataset ######################################
with h5py.File('datatrain.h5', 'r') as hf:
    data = hf['datatrain'][:]

x_train = data

p=os.path.abspath('C:\\Users\\Vicky\\Desktop\\Courses\\Avi\\erisk collections_2017_2018\\erisk collections\\2018\\task 1')
os.chdir(p)

y_test = pd.read_excel('y_test2018.xlsx', sheetname='sheet1')

with h5py.File('datatestbasic2018.h5', 'r') as hf:
    data1 = hf['datatest'][:]

x_test = data1

############# Read Second Dataset ###############
p=os.path.abspath('C:\\Users\\Vicky\\Desktop\\Courses\\Avi\\erisk collections_2017_2018\\erisk collections\\2017\\2test')
os.chdir(p)
with h5py.File('datatrain2.h5', 'r') as hf:
    n1data = hf['datatrain'][:]

p=os.path.abspath('C:\\Users\\Vicky\\Desktop\\Courses\\Avi\\erisk collections_2017_2018\\erisk collections\\2018\\task 1')
os.chdir(p)
with h5py.File('datatest2018_features.h5', 'r') as hf:
    data2 = hf['datatest'][:]

x_train=n1data
for i in range (0,len(x_train),1):
    x_train[i][28917] = x_train[i][28917]*len(x_train)
y_train.ravel()

N_rows=len(y_test);
N_cols=len(x_train[0]);
x_test=np.zeros((N_rows,N_cols))
for i in range(0,len(x_test), 1):
    i
    for j in range(1,28917,1):
        if (j<28914):
            x_test[i][j] = data1[i][j]
        elif (j==28917):
            x_test[i][j] = data2[i][j-28913]*len(x_train)
        else:
            x_test[i][j] = data2[i][j-28913]


##########################################################
###################Results NN#############################
##1st Dataset
accuracy_score=0.9024390243902439
[740   1]
[ 79   0]]
        classification_report(y_test, y_pred)
              precision    recall  f1-score   support

           0       0.90      1.00      0.95       741
           1       0.00      0.00      0.00        79

   micro avg       0.90      0.90      0.90       820
   macro avg       0.45      0.50      0.47       820
weighted avg       0.82      0.90      0.86       820

#2nd Dataset
accuracy=0.8975609756097561
[736   5]
[ 79   0]
        classification_report(y_test, y_pred))
              precision    recall  f1-score   support

           0       0.90      0.99      0.95       741
           1       0.00      0.00      0.00        79

   micro avg       0.90      0.90      0.90       820
   macro avg       0.45      0.50      0.47       820
weighted avg       0.82      0.90      0.85       820