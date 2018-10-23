#!/usr/bin/python3
import matplotlib.pyplot as plt


def plotpixels(title, d):
    x = []
    y = []
    for item in d:
        x.append(item[0])
        y.append(item[1])
    plt.axis([0, 1440, 2560, 0])
    plt.scatter(x, y, s=1)
    plt.title(title)
    plt.show()