#!/usr/bin/python3
import math
import numpy as np


def direction(d):
    three_points = []
    direct = []
    for i in range(0, len(d), 3):
        j = i
        while j < (i + 3) and j < len(d):
            three_points.append(d[j])
            j = j + 1
        if len(three_points) == 3:
            direct.append(calculate_direction(three_points))
        three_points = []
    final_direct = np.std(direct)
    return final_direct


def calculate_direction(list):
    x1 = list[0][0] - list[2][0]
    y1 = list[0][1] - list[2][1]
    s = math.sqrt(x1 * x1 + y1 * y1)
    if s != 0:
        cos = x1 / s
    else:
        cos = 0.0
    alpha = math.acos(min(max(cos, -1.0), 1.0))
    if 0 <= alpha < 2 * math.pi:
        return alpha
    else:
        return 0
