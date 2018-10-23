#!/usr/bin/python3
from PreprocessingCodes.showpoints import showpoints
from PreprocessingCodes.interpolation import interpolation
from FeatureExtractionCodes.features import features
import csv
import os

def preProcessing(filename, folderPath):
    d = showpoints('Original Plot', filename, folderPath)
    d = interpolation(d)
    final_features = features(d)
    print(filename[0:2])
    target = int(filename[0:2])
    final_features.insert(0, target)
    
    # print(final_features)
    # print(len(final_features))


    title_row = ['Label']
    for i in range(360):
        title_row.append(i + 1)
    filename = os.path.expanduser("training_dataset.csv")
    # print(filename)
    if os.path.exists(filename):
        # print('exists')
        append_write = 'a' # append if already exists...
    else:
        # print('not exist')
        append_write = 'w+' # make a new file if not

    myFile = open(filename, append_write, newline='')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerow(final_features)
    myFile.close()
    # d = smoothing(d, 4, filename)

path = input('Enter the folder path:')

for f in os.listdir(path):
    preProcessing(f, path)




