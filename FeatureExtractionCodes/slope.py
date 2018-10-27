#!/usr/bin/python3
import math


def slope(aspect):
    if len(aspect) > 1:
        x1 = float(aspect[0][0])
        x2 = float(aspect[-1][0])
        y1 = float(aspect[0][1])
        y2 = float(aspect[-1][1])
        dx = x2 - x1
        dy = y2 - y1
        if dx != 0 and dy != 0:
            sl = math.acos(dx / (math.sqrt((dx * dx) + (dy * dy))))
        else:
            sl = 0
        return sl
    else:
        return 0
