import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn import utils

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

clf = SVC(kernel='linear') 
clf.fit(x, y) 



