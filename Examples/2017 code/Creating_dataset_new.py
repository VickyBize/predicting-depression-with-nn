#list subfiles and txt 
newDirName = os.path.abspath('C:\\Users\\Vicky\\Desktop\\Courses\\Avi\\erisk collections_2017_2018\\erisk collections\\2017')
newDirList = os.listdir(newDirName)
print (newDirList)

############################################################
################Collect Training data#######################
############################################################

#change path to subpath for analyzing each chunk
pathname = os.path.join(newDirName, newDirList[0]) 
print (pathname)
os.chdir(pathname)
ListTrain = os.listdir(pathname) #save subfolders
print (ListTrain)
#text analysis for negative examples
pathnameNeg = os.path.join(pathname, ListTrain[0]) #enter negative_examples
os.chdir(pathnameNeg)
ListNeg = os.listdir(pathnameNeg)
dataset=[]
ID=[]
data=[]
night=[]
working_hours=[]
evening=[]
x=0;
for i in range (0,9,1):
    pathnameNegChunk = os.path.join(pathnameNeg, ListNeg[i]) 
    os.chdir(pathnameNegChunk)
    #list subfile's xml files
    newDirName1 = os.path.abspath(pathnameNegChunk)
    Xml_files = os.listdir(newDirName1)
    for j in range (0,len(Xml_files),1):
        print (Xml_files[j])
        data = text_analysis(Xml_files[j])
        ID.insert(x, data[1])
        dataset.insert(x, data[0])
        night.insert(x, data[2])
        working_hours.insert(x, data[3])
        evening.insert(x, data[4])
        x=x+1;

#text analysis for positive examples
n_neg=x;
pathnamePos = os.path.join(pathname, ListTrain[1]) 
os.chdir(pathnamePos)
ListPos = os.listdir(pathnamePos)
data=[]
for i in range (0,9,1):
    pathnamePosChunk = os.path.join(pathnamePos, ListPos[i]) 
    os.chdir(pathnamePosChunk)
    #list subfile's xml files
    newDirName1 = os.path.abspath(pathnamePosChunk)
    Xml_files = os.listdir(newDirName1)
    for j in range (0,len(Xml_files),1):
        print (Xml_files[j])
        data = text_analysis(Xml_files[j])
        ID.insert(x, data[1])
        dataset.insert(x, data[0])
        night.insert(x, data[2])
        working_hours.insert(x, data[3])
        evening.insert(x, data[4])
        x=x+1;

#save same ids to txt
#os.chdir(pathname)
#import sys
#orig_stdout = sys.stdout
#f = open('out_train.txt', 'w')
#sys.stdout = f
#for dup in sorted(list_duplicates(ID)):
#    print (dup[0],dup[1])
#
#sys.stdout = orig_stdout
#f.close()

###########################################################
################Collect Testing data#######################
###########################################################

#change path to subpath for analyzing each chunk
pathname = os.path.join(newDirName, newDirList[1]) 
os.chdir(pathname)
ListTest = os.listdir(pathname) #save subfolders

dataset_test=[]
ID_test=[]
data_test=[]
night_test=[]
working_hours_test=[]
evening_test=[]
x_t=0;
for i in range (0,9,1):
    pathnameTestChunk = os.path.join(pathname, ListTest[i]) 
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
#f = open('out_test.txt', 'w')
#sys.stdout = f

#for dup in sorted(list_duplicates(ID_test)):
#    print (dup[0],dup[1])

#sys.stdout = orig_stdout
#f.close()

###########################################################
##add words of the same subjects##
###########################################################

#ids of training sample
os.chdir('C:\\Users\\Vicky\\Desktop\\Courses\\Avi\\erisk collections_2017_2018\\erisk collections\\2017\\1train')
filename = 'out_train.txt'

# Using the newer with construct to close the file automatically.
with open(filename) as f:
    IDtrain = f.readlines()

for i in range (0,len(IDtrain),1):
    IDtrain[i]=IDtrain[i].replace("[", "") 
    IDtrain[i]=IDtrain[i].replace("]", "") 
    IDtrain[i]=IDtrain[i].replace(",", "")
    IDtrain[i]=IDtrain[i].replace("\n", "")
    IDtrain[i]=IDtrain[i].split(" ")

#find the same posts from dataset
datatrain=Counter()
for i in range(0,len(IDtrain), 1):
    datatrain[i]=check_id(IDtrain[i],dataset)

night_train=[]
night1=[]
for i in range(0,len(IDtrain), 1):
    night1=add_id_hours(IDtrain[i],night)
    night_train.insert(i,night1)

workhours_train=[]
workh=[]
for i in range(0,len(IDtrain), 1):
    workh=add_id_hours(IDtrain[i],working_hours)
    workhours_train.insert(i,workh)

even=[]
evening_train=[]
for i in range(0,len(IDtrain), 1):
    even=add_id_hours(IDtrain[i],evening)
    evening_train.insert(i,even)

len(datatrain)
n_train=len(IDtrain)

###############################################


###############################################
#ids of testing sample
os.chdir('C:\\Users\\Vicky\\Desktop\\Courses\\Avi\\erisk collections_2017_2018\\erisk collections\\2017\\1train')
filename = 'out_test.txt'

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

night_test=[]
night1=[]
for i in range(0,len(IDtest), 1):
    night1=add_id_hours(IDtest[i],night)
    night_test.insert(i,night1)

workhours_test=[]
workh=[]
for i in range(0,len(IDtest), 1):
    workh=add_id_hours(IDtest[i],working_hours)
    workhours_test.insert(i,workh)

even=[]
evening_test=[]
for i in range(0,len(IDtest), 1):
    even=add_id_hours(IDtest[i],evening)
    evening_test.insert(i,even)

len (datatest)
n_test=len(IDtest)

############################################################
#Save txt files to see if the user is diagnosed with depression and how many posts they have
#training data

pathname = os.path.join(newDirName, newDirList[0]) 
os.chdir(pathname)
R= open('risk_golden_truth.txt').read()
R1=R.split()
risk_train=np.reshape(R1, (n_train, 2))

N= open("writings-per-subject-all-train.txt").read()
N1=N.split()
Var_train=np.reshape(N1, (n_train, 2))

#testing data
pathname = os.path.join(newDirName, newDirList[1]) 
os.chdir(pathname)
R= open('test_golden_truth.txt').read()
R1=R.split()
risk_test=np.reshape(R1, (n_test, 2))

N= open("writings_all_test_users.txt").read()
N1=N.split()
Var_test=np.reshape(N1, (n_test, 2))

###############################################################
#Save depression marks per ID
#training data
ID_dep_train=[]
dep_train=[]
for j in range (0,len(risk_train),1):
    index=depression_diagnosed(IDtrain[j][0],risk_train)
    ID_dep_train.insert(j, index[0])
    dep_train.insert(j, index[1])

#testing data
ID_dep_test=[]
dep_test=[]
for j in range (0,len(risk_test),1):
    index=depression_diagnosed(IDtest[j][0],risk_test)
    ID_dep_test.insert(j, index[0])
    dep_test.insert(j, index[1])

###############################################################
#Save total numbers of posts per ID
#training data
ID_posts_train=[]
posts_train=[]
for j in range (0,len(Var_train),1):
    index=total_posts(IDtrain[j][0],Var_train)
    ID_posts_train.insert(j, index[0])
    posts_train.insert(j, index[1])

#testing data
ID_posts_test=[]
posts_test=[]
for j in range (0,len(Var_test),1):
    index=total_posts(IDtest[j][0],Var_test)
    ID_posts_test.insert(j, index[0])
    posts_test.insert(j, index[1])

####################################################################
#Create the collection's bag of words

sumbags=Counter()
for i in range(0, len(datatrain), 1):
    sumbags = sumbags+datatrain[i] 

#delete the words that appeared once in total training posts
j=0;
data=[]
for k,v in sumbags.items():
    print (k,v)
    if (v!=1) & (v!=2):
        data.insert(j, [k,v])
        j=j+1;

import xlwt
import openpyxl
import pandas as pd
data1 = pd.DataFrame(data)
############Training#########################################
# Limits to dataframe

N = len(datatrain)
M = len(data1)
# Create the DataFrame with N rows and M columns -- all zeros
newDF = pd.DataFrame(np.zeros((N, M)))
df2=data1
df2 = pd.DataFrame(df2)
for i in range (0,len(datatrain),1):#
    M=len(datatrain[i]);
    df1 = pd.DataFrame(np.zeros((M, 2)))
    print (i)
    j=0;
    sum1=0;
    for k,v in datatrain[i].items():
        df1.iloc[j,0]=k
        df1.iloc[j,1]=v
        sum1=sum1+v;
        j=j+1
    #gives us the intersection of the 2 dataframes to a dataframe with 1st column the total words, 2nd the total appearances,3rd the user's #words
    df3=df2.merge(df1 ,how='left', on=0)
    #same the results to a dataframe with the data of all users
    df3 = df3.fillna(0)
    for x in range (0,len(df3),1):
        newDF.iloc[i,x]=df3.iloc[x,2]/sum1; #term frequency

############Testing#########################################
# Limits to dataframe

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
df = newDF.fillna(0)
df1 = newDF1.fillna(0)

####Save dataset################################################
import h5py
with h5py.File('datatrain.h5', 'w') as hf:
    hf.create_dataset("datatrain",  data=df)

with h5py.File('datatest_basic2017.h5', 'w') as hf:
    hf.create_dataset("datatest",  data=df1)



#################################################################
############# Read Dataset ######################################
with h5py.File('datatrain.h5', 'r') as hf:
    data = hf['datatrain'][:]

with h5py.File('datatest.h5', 'r') as hf:
    data1 = hf['datatest'][:]


#################################################################
#Collect simple dataset
y_train=dep_train
y_test=dep_test

x_train = data
x_test =data1 

#################################################################
#Collect dataset with total posts

train_dataset = pd.DataFrame(np.zeros((len(ID_posts_train), 28918)))
#sumd=0;
#for i in range (0,len(ID_posts_train),1):
#    sumd=sumd+int(posts_train[i])
sumd=295023;
for i in range (0,len(ID_posts_train),1):
    for j in range (0,28914,1):
        train_dataset.iloc[i][j]=data[i][j]
    b=night_train[i]+workhours_train[i]+evening_train[i]
    train_dataset.iloc[i][j+1]=night_train[i]/b
    train_dataset.iloc[i][j+2]=workhours_train[i]/b
    train_dataset.iloc[i][j+3]=evening_train[i]/b
    a=posts_train[i]
    train_dataset.iloc[i][j+4]=int(a)/sumd

test_dataset = pd.DataFrame(np.zeros((len(ID_posts_test), 28918)))
for i in range (0,len(ID_posts_test),1):
    for j in range (0,28914,1):
        test_dataset.iloc[i][j]=data1[i][j]
    b=night_test[i]+workhours_test[i]+evening_test[i]
    test_dataset.iloc[i][j+1]=night_test[i]/b
    test_dataset.iloc[i][j+2]=workhours_test[i]/b
    test_dataset.iloc[i][j+3]=evening_test[i]/b
    test_dataset.iloc[i][j+4]=int(posts_test[i])/sumd

##write extra features to h5py

#with h5py.File('datatest_basic2017_n_w_e_tp.h5', 'w') as hf:
#    hf.create_dataset("datatest",  data=test_dataset)

####Save new dataset################################################
#y1_train = pd.DataFrame(y_train)
#y1_test= pd.DataFrame(y_test)
#y1_train.to_excel('y_train.xlsx', sheet_name='sheet1', index=False)
#y1_test.to_excel('y_test.xlsx', sheet_name='sheet1', index=False)

with h5py.File('datatrain_2017_n_w_e_tp.h5', 'w') as hf:
    hf.create_dataset("datatrain",  data=train_dataset.values)

with h5py.File('datatest_2017_n_w_e_tp.h5', 'w') as hf:
    hf.create_dataset("datatest",  data=test_dataset.values)

#################################################################
############# Read Dataset ######################################
with h5py.File('datatrain_2017_n_w_e_tp.h5', 'r') as hf:
    n1data = hf['datatrain'][:]
with h5py.File('datatest_2017_n_w_e_tp.h5', 'r') as hf:
    n1data1 = hf['datatest'][:]

y_train = pd.read_excel('y_train.xlsx', sheetname='sheet1')
y_test = pd.read_excel('y_test.xlsx', sheetname='sheet1')
x_train=n1data
x_test=n1data1
