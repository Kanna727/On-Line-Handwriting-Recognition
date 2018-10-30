from PreprocessingCodes.interpolation import interpolation
from FeatureExtractionCodes.features import features
from test_code import predictStrokeLabel
import matplotlib.pyplot as plt


strokesList=[]
tempStrokeList=[]
strokeLabelsList = []

path = input('Enter the file path:')

with open(path) as f:
    content = f.readlines()

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
    strokeLabel = predictStrokeLabel(final_features)
    print(strokeLabel)
    strokeLabelsList.append(strokeLabel)

strokeLabelsList.sort()

print(strokeLabelsList)
