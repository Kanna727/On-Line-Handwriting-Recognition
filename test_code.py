import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn import utils

def predictStrokeLabel(featuresList,clf):
    

    result = clf.predict([featuresList])

    return int(result[0])
