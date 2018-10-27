import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

x=pd.read_csv("training_dataset.csv")
a=np.array(x)
y=a[:]

x.shape

print (x),(y)

