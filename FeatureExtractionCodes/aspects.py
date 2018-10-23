#!/usr/bin/python3
from FeatureExtractionCodes.curliness import curliness
from FeatureExtractionCodes.linearity import linearity
from FeatureExtractionCodes.slope import slope
import numpy as np
from FeatureExtractionCodes.direction import direction
from FeatureExtractionCodes.curvature import curvature


def aspects(d):
    l = []
    strokes_list = []
    
    sz = len(d)
    
    j = 1
    
    for coordinate in d:
        if coordinate[2] == 0.0:
            l.append(coordinate)
        else:
            strokes_list.append(l)
            l = []
    # print(len(strokes_list))
    # for item in strokes_list:
    #     print(len(item))
    
    stroke_wise_aspects_list = []
    full_aspects_list = []
    stroke_wise_features_list = []
    for stroke in strokes_list:
        final_direct = direction(stroke)
        final_curv = curvature(stroke)
        single_aspect = []
        sz_stroke = len(stroke)
        curl = []
        lin = []
        sl = []
        for i in range(0, sz_stroke, 10):
            j = i
            while j < (i + 10) and j < sz_stroke:
                single_aspect.append(stroke[j])
                j = j + 1
            curl.append(curliness(single_aspect))
            lin.append(linearity(single_aspect))
            sl.append(slope(single_aspect))
            stroke_wise_aspects_list.append(single_aspect)
            single_aspect = []
        final_curl = np.std(curl)
        final_lin = np.std(lin)
        final_sl = np.std(sl)
        stroke_wise_features_list.append([final_curl, final_lin, final_sl, final_direct, final_curv])
        full_aspects_list.append(stroke_wise_aspects_list)
        stroke_wise_aspects_list = []
    return stroke_wise_features_list
