import os
import re
import sys
import numpy as np
from collections import Counter
import collections
import h5py
import pandas as pd

newDirName = os.path.abspath('C:\\Users\\Vicky\\Desktop\\Courses\\Μηχανες Αναζητησης\\erisk collections_2017_2018\\erisk collections\\2017')
newDirList = os.listdir(newDirName)
print (newDirList)
#change path to subpath 
pathname = os.path.join(newDirName, newDirList[1]) 
os.chdir(pathname)
ListTest = os.listdir(pathname)

#############Read Output ###############################################
y_train = pd.read_excel('y_train.xlsx', sheetname='sheet1')
y_test = pd.read_excel('y_test.xlsx', sheetname='sheet1')

############# Read First Dataset ######################################
with h5py.File('datatrain.h5', 'r') as hf:
    data = hf['datatrain'][:]

with h5py.File('datatest.h5', 'r') as hf:
    data1 = hf['datatest'][:]

x_train = data
x_test =data1 

############# Read Second Dataset ######################################
with h5py.File('datatrain2.h5', 'r') as hf:
    n1data = hf['datatrain'][:]

with h5py.File('datatest2.h5', 'r') as hf:
    n1data1 = hf['datatest'][:]

x_train=n1data
for i in range (0,len(x_train),1):
    x_train[i][28917] = x_train[i][28917]*len(x_train)
y_train.ravel()
x_test=n1data1
for i in range (0,len(x_test),1):
    x_test[i][28917] = x_test[i][28917]*len(x_train)

##########################################################
###################Results NN#############################
##1st Dataset
accuracy_score = 0.885286783042394
confusion_matrix =  [342   7]
                    [ 39  13]

                   classification_report
              precision    recall  f1-score   support

           0       0.90      0.98      0.94       349
           1       0.65      0.25      0.36        52

   micro avg       0.89      0.89      0.89       401
   macro avg       0.77      0.61      0.65       401
weighted avg       0.87      0.89      0.86       401

#2nd Dataset
accuracy_score=0.9152119700748129
confusion_matrix =  [340   9]
                    [ 25  27]
                classification_report
              precision    recall  f1-score   support

           0       0.93      0.97      0.95       349
           1       0.75      0.52      0.61        52

   micro avg       0.92      0.92      0.92       401
   macro avg       0.84      0.75      0.78       401
weighted avg       0.91      0.92      0.91       401