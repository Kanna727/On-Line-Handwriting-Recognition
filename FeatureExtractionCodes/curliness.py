#!/usr/bin/python3
import math


def curliness(aspect):
    if len(aspect) > 1:
        total_length = 0
        for i in range(0, len(aspect) - 1, 2):
            dx = float(aspect[i][0]) - float(aspect[i + 1][0])
            dy = float(aspect[i][1]) - float(aspect[i + 1][1])
            d = math.sqrt((dx * dx) + (dy * dy))
            total_length = total_length + d
        first = aspect[0]
        last = aspect[-1]
        dx = abs(float(first[0]) - float(last[0]))
        dy = abs(float(first[1]) - float(last[1]))
        denom = max(dx, dy)
        if denom != 0:
            curl = (total_length/denom) - 2
        else:
            curl = 0
        if -1 <= curl <= 1:
            return curl
        else:
            return 0
    else:
        return 0
