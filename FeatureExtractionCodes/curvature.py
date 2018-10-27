#!/usr/bin/python3
from FeatureExtractionCodes.direction import direction
from FeatureExtractionCodes.direction import calculate_direction
import math
import numpy as np


def curvature(d):
    five_points = []
    direct = []
    for i in range(0, len(d), 5):
        j = i
        while j < (i + 5) and j < len(d):
            five_points.append(d[j])
            j = j + 1
        if len(five_points) == 5:
            direct.append(calculate_curvature(five_points))
        five_points = []
    final_direct = np.std(direct)
    return final_direct


def calculate_curvature(l):
    first_three_points = []
    last_three_points = []
    first_three_points.extend([l[0], l[1], l[2]])
    last_three_points.extend([l[2], l[3], l[4]])
    cos = (math.cos(calculate_direction(first_three_points) * math.cos(calculate_direction(last_three_points)))) +\
          (math.sin(calculate_direction(first_three_points) * math.sin(calculate_direction(last_three_points))))
    if -1 <= cos <= 1:
        beta = math.acos(cos)
        return beta
    else:
        return 0
