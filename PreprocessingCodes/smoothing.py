#!/usr/bin/python3
from PreprocessingCodes.resampling import resampling
from PreprocessingCodes.plotpixels import plotpixels


# cook your code here
def smoothing(d, div, filename):  # d is a 2d list, div is 4
    sz = len(d)  # no. of rows in d, i.e, no. of coordinates
    t = [[0 for x in range(3)] for y in range(sz)]  # 2d list with all zeros
    x_coor = []
    y_coor = []
    for j in range(sz):  # this loop makes a list of all x coordinates
        x_coor.append((d[j][0]))
    max_x = max(x_coor)  # max and min values of x coordinate
    min_x = min(x_coor)
    for j in range(sz):  # this loop makes a list of all y coordinates
        y_coor.append((d[j][1]))
    max_y = max(y_coor)  # max and min values of y coordinate
    min_y = min(y_coor)
    width = max_x - min_x
    height = max_y - min_y
    density = (width * height) / sz
    ip = round(density / div)  # helps to divide strokes in two portions
    for i in range(sz):
        j = i - 1
        avgx = avgy = a = b = 0
        while j >= 0 and i - j <= ip:  # first portion
            if d[j][2] < 1:  # pen writing
                avgx += d[j][0]
                avgy += d[j][1]
                a = a + 1
                j = j - 1
            else:
                break
        j = i + 1
        while j <= i + ip and j - i <= a and j < sz:  # second portion
            if d[j][2] < 1:  # pen writing
                avgx += d[j][0]
                avgy += d[j][1]
                b = b + 1
                j = j + 1
            else:
                break
        if a > b:
            j = i - b - 1
            while j >= (i - a):
                avgx -= d[j][0]
                avgy -= d[j][1]
                j = j - 1
        avgx += d[i][0]
        avgy += d[i][1]
        b = (2 * b) + 1
        t[i][0] = round(avgx / b)
        t[i][1] = round(avgy / b)
        t[i][2] = d[i][2]
    #print(t)
    d = resampling(t)  # updating matrix after smoothing and resampling
    s = len(d)
    # fid=open(filename,"w+") #upadted coordinate file
    # for i in range(s):
    # fid.write("%d %d %d\n" % (d[i][0],d[i][1],d[i][2]))
    # fid.close()
    plotpixels('After Smoothing', d)  # plot pixels after smoothing
    return d
