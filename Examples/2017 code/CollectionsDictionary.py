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

len(datatrain)
n_train=len(IDtrain)

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