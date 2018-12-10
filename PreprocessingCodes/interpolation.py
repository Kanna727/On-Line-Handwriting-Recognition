#!/usr/bin/python3
# cook your code here
import math
import numpy as np
from PreprocessingCodes.plotpixels import plotpixels
from PreprocessingCodes.resampling import resampling


def interpolation(d):
    B = d[:]  # copying the 2d list by slicing it from beginning to end
    sz = len(d)
    t = [d[0]]  # the fisrt x, y and pen position
    for i in range(1, sz):
        if B[i][2] == 0 and B[i - 1][2] == 0:  # when pen is moving
            x1 = B[i][0]
            y1 = B[i][1]
            x2 = B[i - 1][0]
            y2 = B[i - 1][1]
            pix = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # difference of pixels in the adjacent points
            if pix == 0:  # both adjacent points are same
                continue
            sz = 1 / pix
            ran = np.arange(0.0, 1.0, sz)
            for k in ran:  # k goes from 0 to 1, 1+sz is exclusive ,k has increament of sz after every loop
                # 1+sz as second argument in range is wrong I think since k can get value between 1 and 1+sz
                # and that time loop will run,which shouldn't be, what should be given there?
                x = B[i - 1][0] * (1 - k) + B[i][0] * k
                y = B[i - 1][1] * (1 - k) + B[i][1] * k
                t.append([round(x), round(y), 0])  # 2d list, first row has initial t list(1d)

        if B[i][2] == 1:  # pen down
            t.append([B[i][0], B[i][1], 1])  # 2d list , no change in coordinates
    d = resampling(t)
    #print(d)
    plotpixels('After Preprocessing', d)
    return t
