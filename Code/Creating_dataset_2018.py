#list subfiles and txt 
newDirName = os.path.abspath('C:\\Users\\Vicky\\Desktop\\Courses\\Avi\\erisk collections_2017_2018\\erisk collections\\2018\\task 1')
newDirList = os.listdir(newDirName)
print (newDirList)

###########################################################
################Collect Testing data#######################
###########################################################

#change path to subpath for analyzing each chunk
ListTest = os.listdir(newDirName) #save subfolders
pathname=newDirName;

dataset_test=[]
ID_test=[]
data_test=[]
night_test=[]
working_hours_test=[]
evening_test=[]
x_t=0;
for i in range (0,9,1):
    pathnameTestChunk = os.path.join(pathname, ListTest[i+1]) 
    os.chdir(pathnameTestChunk)
    #list subfile's xml files
    newDirName1 = os.path.abspath(pathnameTestChunk)
    Xml_files = os.listdir(newDirName1)
    for j in range (0,len(Xml_files),1):
        print (Xml_files[j])
        data_test = text_analysis(Xml_files[j])
        ID_test.insert(x_t, data_test[1])
        dataset_test.insert(x_t, data_test[0])
        night_test.insert(x_t, data_test[2])
        working_hours_test.insert(x_t, data_test[3])
        evening_test.insert(x_t, data_test[4])
        x_t=x_t+1;

n=x_t

#os.chdir(pathname)
#import sys
#orig_stdout = sys.stdout
#f = open('out_test2018.txt', 'w')
#sys.stdout = f

#for dup in sorted(list_duplicates(ID_test)):
#    print (dup[0],dup[1])

#sys.stdout = orig_stdout
#f.close()

###########################################################
##add words of the same subjects##
###########################################################
p=os.path.abspath('C:\\Users\\Vicky\\Desktop\\Courses\\Avi\\erisk collections_2017_2018\\erisk collections\\2018\\task 1')
os.chdir(p)
#ids of testing sample
filename = 'out_test2018.txt'

# Using the newer with construct to close the file automatically.
with open(filename) as f:
    IDtest = f.readlines()

for i in range (0,len(IDtest),1):
    IDtest[i]=IDtest[i].replace("[", "") 
    IDtest[i]=IDtest[i].replace("]", "") 
    IDtest[i]=IDtest[i].replace(",", "")
    IDtest[i]=IDtest[i].replace("\n", "")
    IDtest[i]=IDtest[i].split(" ")

#find the same posts from dataset_test
datatest=Counter()
for i in range(0,len(IDtest), 1):
    datatest[i]=check_id(IDtest[i],dataset_test)

night=night_test
night_test=[]
night1=[]
for i in range(0,len(IDtest), 1):
    night1=add_id_hours(IDtest[i],night)
    night_test.insert(i,night1)

working_hours=working_hours_test
workhours_test=[]
workh=[]
for i in range(0,len(IDtest), 1):
    workh=add_id_hours(IDtest[i],working_hours)
    workhours_test.insert(i,workh)

evening=evening_test
evening_test=[]
even=[]
for i in range(0,len(IDtest), 1):
    even=add_id_hours(IDtest[i],evening)
    evening_test.insert(i,even)

len (datatest)
n_test=len(IDtest)

############################################################
#Save txt files to see if the user is diagnosed with depression and how many posts they have
#testing data

os.chdir(newDirName)
R= open('risk-golden-truth-test.txt').read()
R1=R.split()
risk_test=np.reshape(R1, (n_test, 2))

N= open('writings-per-subject-all-test.txt').read()
N1=N.split()
Var_test=np.reshape(N1, (n_test, 2))

###############################################################
#Save depression marks per ID
#testing data
ID_dep_test=[]
dep_test=[]
for j in range (0,len(risk_test),1):
    index=depression_diagnosed(IDtest[j][0],risk_test)
    ID_dep_test.insert(j, index[0])
    dep_test.insert(j, index[1])

###############################################################
#Save total numbers of posts per ID
#testing data
ID_posts_test=[]
posts_test=[]
for j in range (0,len(Var_test),1):
    index=total_posts(IDtest[j][0],Var_test)
    ID_posts_test.insert(j, index[0])
    posts_test.insert(j, index[1])

############Testing#########################################
# Limits to dataframe

import xlwt
import openpyxl
import pandas as pd
import h5py
data1 = pd.read_excel('CollectionsDictionary.xlsx', sheetname='Words')

N = len(datatest)
M = len(data1)
# Create the DataFrame with N rows and M columns -- all zeros
newDF1 = pd.DataFrame(np.zeros((N, M)))
df2=data1

for i in range (0,len(datatest),1):
    df2=data1
    M=len(datatest[i]);
    df1 = pd.DataFrame(np.zeros((M, 2)))
    print (i)
    j=0;
    sum1=0;
    for k,v in datatest[i].items():
        df1.iloc[j,0]=k
        df1.iloc[j,1]=v
        sum1=sum1+v;
        j=j+1
    #gives us the intersection of the 2 dataframes to a dataframe with 1st column the total words, 2nd the total appearances,3rd the user's #words
    df3=df2.merge(df1 ,how='left', on=0)
    #same the results to a dataframe with the data of all users
    df3 = df3.fillna(0)
    for x in range (0,len(df3),1):
        newDF1.iloc[i,x]=df3.iloc[x,2]/sum1; #term frequency

#remove nan cells
df1 = newDF1.fillna(0)

####Save dataset################################################
import h5py
with h5py.File('datatestbasic2018.h5', 'w') as hf:
    hf.create_dataset("datatest",  data=df1)



#################################################################
############# Read Dataset ######################################
with h5py.File('datatestbasic2018.h5', 'r') as hf:
    data1 = hf['datatest'][:]


#################################################################
#Collect simple dataset
#y_train=dep_train
y_test=dep_test

#x_train = data
x_test =data1 

#################################################################
#Collect dataset with total posts

sumd=295023;

import numpy as np
import pandas as pd
N_rows=len(ID_posts_test);
N_cols=len(data1[0])+4;

test_dataset = pd.DataFrame(np.zeros((N_rows, N_cols)))

for i in range (0,len(ID_posts_test),1):
    for j in range (0,28914,1):
        test_dataset.iloc[i][j]=data1[i][j]
    b=night_test[i]+workhours_test[i]+evening_test[i]
    test_dataset.iloc[i][0]=night_test[i]/b
    test_dataset.iloc[i][1]=workhours_test[i]/b
    test_dataset.iloc[i][2]=evening_test[i]/b
    test_dataset.iloc[i][3]=int(posts_test[i])/sumd

####Save new dataset################################################
#y1_train = pd.DataFrame(y_train)
y1_test= pd.DataFrame(y_test)
#y1_train.to_excel('y_train.xlsx', sheet_name='sheet1', index=False)
y1_test.to_excel('y_test2018.xlsx', sheet_name='sheet1', index=False)

#with h5py.File('datatrain2.h5', 'w') as hf:
#    hf.create_dataset("datatrain",  data=train_dataset.values)

with h5py.File('datatest2018_features.h5', 'w') as hf:
    hf.create_dataset("datatest",  data=test_dataset.values)

#################################################################
############# Read Dataset ######################################
with h5py.File('datatrain2.h5', 'r') as hf:
    n1data = hf['datatrain'][:]
with h5py.File('datatest2018_with features.h5', 'r') as hf:
    n1data1 = hf['datatest'][:]

y_train = pd.read_excel('y_train.xlsx', sheetname='sheet1')
y_test = pd.read_excel('y_test.xlsx', sheetname='sheet1')
x_train=n1data
x_test=n1data1
