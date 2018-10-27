#!/usr/bin/python3
def resampling(t):
    b = t
    b_size = len(b)
    t = [b[0]]

    for i in range(1, b_size):
        if b[i-1][0] == b[i][0] and b[i-1][1] == b[i][1]:
            if b[i][2] == 1:
                t.append(b[i])
        else:
            t.append(b[i])

            
    return t
