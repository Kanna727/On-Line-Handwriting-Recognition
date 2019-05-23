from PreprocessingCodes.interpolation import interpolation
from FeatureExtractionCodes.features import features
#from test_code import predictStrokeLabel
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn import utils
def strokeSeg(content):
    strokesList = []
    tempStrokeList=[]
    strokeLabelsList = []
    def predictStrokeLabel(featuresList):
  

       result = clf.predict([featuresList])

       return int(result[0])
    # folderPath = 'C:\\Users\\DEDSEC\\OneDrive\\Documents\\VSCode\\Minor Project\\On-Line-Handwriting-Recognition\\Letter Test Samples\\Working'

    # fileName = input('Enter the file name:')
    # path = folderPath + '\\'+ fileName

    # with open(path) as f:
    #     content = f.readlines()
    x=pd.read_csv("training_dataset.csv")
    print(np.isnan(x))

    c = np.array(x)
    y = c[:,0]
    x.drop(["Class"], axis=1,inplace=True)
    a=np.array(x)

    lab_enc = preprocessing.LabelEncoder()
    clf = SVC(C=1.0, kernel='poly',degree=3, gamma=2)
    clf.fit(x, y)     


    content = [z.strip().split(',') for z in content]
    for item in content:
        if(item[2]=='0'):
            item[0]=float(item[0])
            item[1]=float(item[1])
            item[2]=float(item[2])
            tempStrokeList.append(item)
        else:
            strokesList.append(tempStrokeList)
            tempStrokeList=[]

    #print(strokesList[1])
    for stroke in strokesList:
        
        s = interpolation(stroke)
        final_features = features(s)
        strokeLabel = predictStrokeLabel(final_features,clf)
        print(strokeLabel)
        strokeLabelsList.append(strokeLabel)

    strokeLabelsList.sort()

    #return strokeLabelsList
    strLabel = '.'.join(str(e) for e in strokeLabelsList)
    print(strLabel)

    fo = open("hindidic.txt", "r",encoding="utf8")

 #letter = ["पुनः पय।स करें।"]
    letter= ["Try"]
    for i in fo:
     i=i.rstrip() #returns each line as string removing the last \n character
     if strLabel == i:
      letter[0] =next(fo).rstrip()
    # print(next(fo), end='')
      break
    fo.close()

# compareLabel(strokeLabelsList)
# return strokeLabelsList

    return letter
    

#print(letter)
