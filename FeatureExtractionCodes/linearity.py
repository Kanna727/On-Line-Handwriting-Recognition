#!/usr/bin/python3
import math


def linearity(aspect):
    if len(aspect) > 1:
        first = aspect[0]
        last = aspect[-1]
        a = float(last[1]) - float(first[1])
        b = float(last[0]) - float(first[0])
        c = (float(last[0]) * float(first[1])) - (float(first[0]) * float(last[1]))
        s = 0
        for point in aspect:
            if a != 0 and b != 0:
                x = float(point[0])
                y = float(point[1])
                d = ((a * x) + (b * y) + c) / (math.sqrt((a * a) + (b * b)))
                s = s + (d * d)
        lin = s / len(aspect)
        return lin
    else:
        return 0
