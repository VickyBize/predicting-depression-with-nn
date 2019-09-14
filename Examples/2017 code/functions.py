import os
import re
import sys
import numpy as np
import nltk
import xml.etree.ElementTree as ET
from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()
from nltk.stem import PorterStemmer
ps = PorterStemmer()
from nltk.corpus import stopwords
from collections import Counter
import collections
import time
from time import mktime
from datetime import datetime
from collections import defaultdict


def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items() 
            if len(locs)>1)

def add_id_hours(IDs,timezone):
    print (IDs[0])
    sumTimezone=int()
    for j in range(1, len(IDs), 1):
        sumTimezone = sumTimezone + timezone[int(IDs[j])] 
    return sumTimezone

def check_id(IDs,dataset1):
    print (IDs[0])
    sumbags=Counter()
    for j in range(1, len(IDs), 1):
        sumbags = sumbags+dataset1[int(IDs[j])] 
    return sumbags

def depression_diagnosed(ID, risk_train):
    for i in range (0,len(risk_train),1):
        if ID==risk_train[i][0]:
            a=risk_train[i][1]
            return ID,a

def total_posts(ID, Var_train):
    for i in range (0,len(Var_train),1):
        if ID==Var_train[i][0]:
            a=Var_train[i][1]
            return ID,a

def convAlph2Num(sent):
    alphArray = list(string.ascii_lowercase)
    alphSet = set(alphArray)
    sentArray = list(sent.lower())
    x = ''
    for u in sentArray:
        if u in alphSet:
            u = alphArray.index(u) + 1
            u=str(u)
            x=x+u
    return x

import time
from time import mktime
from datetime import datetime

def getTimeCat(time1):
    # extract time categories
    xml_str = ET.tostring(time1).decode()
    b=xml_str[18]+xml_str[19];
    b=int(b)
    #print (b)
    if (b>=0 and b<8):
        timecat = 1 #night
    elif (b>=8 and b<16):
        timecat = 2 #working hours
    elif (b>=16 and b<24):
        timecat = 3 #evening
    return timecat

