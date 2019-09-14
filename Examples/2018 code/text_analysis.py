def text_analysis(fname):
    tree = ET.parse(fname)
    root = tree.getroot()
 #save all xml data into a
    r = list(root) #get all the data of the tree 
    ID=r[0].text #get the ID of the user
 #save the data within the WRITING
    for child in root: data= root.findall(child.tag+"/*")
 #reshape list to a list with info of every post in one line and the delete the useless columns
    a = [data[i:i+4] for i in range(0, len(data), 4)]
    for row in a:
        del row[0],row[1]
    time = [[a[i][0]] for i in range(0, len(a), 1)]
    posts= [[a[i][1]] for i in range(0, len(a), 1)]
    timeZone=[]
    for i in range (0,len(time),1):
        time1=time[i][0]
        b=getTimeCat(time1)
        timeZone.insert(i,b)
    working_hours=int()
    evening=int()
    night=int()
    for i in range (0,len(timeZone),1):
        if (timeZone[i]==1):
            night = night+1; #night
        elif (timeZone[i]==2):
            working_hours = working_hours+1; #working hours
        elif (timeZone[i]==3):
            evening = evening+1; #evening
#tokenize the 2nd column of a 
    set(stopwords.words('english'))
    b= [tknzr.tokenize(posts[i][0].text) for i in range(0, len(posts), 1)] #tokenize
    words = [[word for word in b[i] if word.isalpha()] for i in range(0, len(b), 1)] #remove ",.
    b1= [[ps.stem(words[i][j]) for j in range(0, len(words[i]), 1)] for i in range(0, len(words), 1)] #stemming
    filtered_words = list(filter(lambda word: word not in stopwords.words('english'), b1)) #stop words
    bagsofwords = [[ collections.Counter(re.findall(r'\w+', txt)) for txt in filtered_words[i]] for i in range(0, len(filtered_words), 1) ]
    sumbags=Counter()
    for i in range(0, len(bagsofwords), 1):
        for j in range(0, len(bagsofwords[i]), 1):
            sumbags = sumbags+bagsofwords[i][j] 
    return [sumbags,ID,night,working_hours,evening]