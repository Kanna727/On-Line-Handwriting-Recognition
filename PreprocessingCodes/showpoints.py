#!/usr/bin/python3
import matplotlib.pyplot as plt
import os


def showpoints(title, filename, folderPath):
    x = []
    y = []
    d = []
    with open(folderPath+'\\'+filename) as f:
        # f.seek(0, os.SEEK_CUR)
        # f.truncate()
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [z.strip().split(',') for z in content]
    for item in content:
        #print("x= ",x)
        d.append(item)
        x.append(float(item[0]))
        y.append(float(item[1]))

    d = [[float(y) for y in x] for x in d]
    plt.axis([0, 1440, 2560, 0])

    # plt.scatter(x, y, s=1)
    # plt.title(title)
    # plt.show()
    return d


