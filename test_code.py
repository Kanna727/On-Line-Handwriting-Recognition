import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn import utils

def predictStrokeLabel(featuresList):
    x=pd.read_csv("training_dataset.csv")
    c = np.array(x)
    y = c[:,0]
    x.drop(["Class"], axis=1,inplace=True)
    a=np.array(x)


    lab_enc = preprocessing.LabelEncoder()

    clf = SVC(C=1.0, kernel='poly',degree=3, gamma=2)
    clf.fit(x, y) 

    result = clf.predict([featuresList])

    return int(result[0])
