#!/usr/bin/python3
from FeatureExtractionCodes.aspects import aspects
from FeatureExtractionCodes.curvature import curvature
from FeatureExtractionCodes.curliness import curliness
from FeatureExtractionCodes.direction import direction
from FeatureExtractionCodes.linearity import linearity
from FeatureExtractionCodes.slope import slope
import math


def features(d):
    # strokes_list = []
    # l = []

    # for coordinate in d:
    #     if coordinate[2] == 0.0:
    #         l.append(coordinate)
    #     else:
    #         strokes_list.append(l)
    #         l = []

    zones = []
    stroke_wise_zones =[]
    zone_features = []

    # fr stroke in strokes_list:
    zone1 = []
    zone2 = []
    zone3 = []
    zone4 = []
    zone5 = []
    zone6 = []
    zone7 = []
    zone8 = []
    zone9 = []
    zone_list = []
    sz = len(d)  # no. of rows in d, i.e, no. of coordinates
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
    #print(min_x, max_x, min_y, max_y)
    dx = max_x - min_x  # Width of the grid
    dy = max_y - min_y  # Height of the grid
    l = dx / 3
    m = 2 * (dx / 3)
    a = dy / 3
    b = 2 * (dy / 3)
    #print(min_x, l + min_x, m + min_x, min_y, a + min_y, b + min_y)
    for point in d:
        if point[0] <= min_x + l:
            if point[1] <= min_y + a:
                zone1.append(point)
            if min_y + a < point[1] <= min_y + b:
                zone4.append(point)
            if point[1] > min_y + b:
                zone7.append(point)
        if min_x + l < point[0] <= min_x + m:
            if point[1] <= min_y + a:
                zone2.append(point)
            if min_y + a < point[1] <= min_y + b:
                zone5.append(point)
            if point[1] > min_y + b:
                zone8.append(point)
        if point[0] > min_x + m:
            if point[1] <= min_y + a:
                zone3.append(point)
            if min_y + a < point[1] <= min_y + b:
                zone6.append(point)
            if point[1] > min_y + b:
                zone9.append(point)
    zone_list.append(zone1)
    zone_list.append(zone2)
    zone_list.append(zone3)
    zone_list.append(zone4)
    zone_list.append(zone5)
    zone_list.append(zone6)
    zone_list.append(zone7)
    zone_list.append(zone8)
    zone_list.append(zone9)
    # print([zone1, zone2, zone3, zone4, zone5, zone6, zone7, zone8, zone9])
    zones = []
    for zone in zone_list:
        vicinity = []
        bin_curl = [0 for x in range(8)]
        bin_lin = [0 for x in range(8)]
        bin_sl = [0 for x in range(8)]
        bin_dir = [0 for x in range(8)]
        bin_curv = [0 for x in range(8)]
        if len(zone) != 0:
            for i in range(0, len(zone), 11):
                j = i
                while j < (i + 11) and j < len(zone):
                    vicinity.append(zone[j])
                    j = j + 1
                bin = quantizer(math.acos(curliness(vicinity)))
                bin_curl[bin] = bin_curl[bin] + 1
                bin = quantizer(math.atan(linearity(vicinity)))
                bin_lin[bin] += 1
                bin = quantizer(slope(vicinity))
                bin_sl[bin] += 1
                vicinity = []
            vicinity = []
            for i in range(0, len(zone), 3):
                j = i
                while j < (i + 3) and j < len(zone):
                    vicinity.append(zone[j])
                    j = j + 1
                bin = quantizer(direction(vicinity))
                bin_dir[bin] += 1
                vicinity = []
            vicinity = []
            for i in range(0, len(zone), 5):
                j = i
                while j < (i + 5) and j < len(zone):
                    vicinity.append(zone[j])
                    j = j + 1
                bin = quantizer(curvature(vicinity))
                bin_curv[bin] += 1
                vicinity = []
            for i in range(8):
                bin_curv[i] /= len(zone)
                bin_dir[i] /= len(zone)
                bin_sl[i] /= len(zone)
                bin_lin[i] /= len(zone)
                bin_curl[i] /= len(zone)
        zone_features.extend(bin_dir)
        zone_features.extend(bin_curv)
        zone_features.extend(bin_sl)
        zone_features.extend(bin_lin)
        zone_features.extend(bin_curl)
    return zone_features


def quantizer(val):
    if 0 <= val < math.pi / 4:
        return 0
    elif math.pi / 4 <= val < math.pi / 2:
        return 1
    elif math.pi / 2 <= val < math.pi * 0.75:
        return 2
    elif math.pi * 0.75 <= val < math.pi:
        return 3
    elif math.pi <= val < math.pi * 1.25:
        return 4
    elif math.pi * 1.25 <= val < math.pi * 1.5:
        return 5
    elif math.pi * 1.5 <= val < math.pi * 1.75:
        return 6
    elif math.pi * 1.75 <= val < math.pi * 2:
        return 7
    else:
        return 0
