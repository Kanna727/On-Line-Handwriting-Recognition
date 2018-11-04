import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn import utils
from PreprocessingCodes.showpoints import showpoints
from PreprocessingCodes.interpolation import interpolation
from FeatureExtractionCodes.features import features

def getFeatures(folderPath, filename):
    d = showpoints('Original Plot', filename, folderPath)
    d = interpolation(d)
    final_features = features(d)
    return final_features

x=pd.read_csv("training_dataset.csv")
#b = x[["Class"]].copy()
c = np.array(x)
y = c[:,0]
#y = np.array(b)
x.drop(["Class"], axis=1,inplace=True)
a=np.array(x)

#p = pd.DataFrame(x).set_index('id')[10].copy(deep=True)


#print(y)


lab_enc = preprocessing.LabelEncoder()
#encoded = lab_enc.fit_transform(y)
#encoded = lab_enc.fit_transform(x)

#clf = SVC(kernel='rbf') 
clf = SVC(C=1.0, kernel='poly',degree=3, gamma=2)
clf.fit(x, y) 

folderPath = input("Enter folder path: ")
fileName = input("Enter file name: ")

features = getFeatures(folderPath, fileName)
print(clf.predict([features]))
print(clf.score(x,y))

"/home/karthik/Documents/vscode/minorproject/On-Line-Handwriting-Recognition/Samples"







