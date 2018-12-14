import numpy as np
from Point import Point


def init_array(w, l, sw, sl, exclusions):     # w = room width, l = room length, sw = segment_width, sl = segment_length
    xr = l % sl                              # remainder of length/segment_length
    lx = int((l - xr)/sl)                    # number of segments along x
    yr = w % sw                              # remainder of width/segment_width
    ly = int((w - yr)/sw)                    # number of segments along y
    data_array = np.empty([ly, lx], object)

    for i in range(len(data_array[:, 0])):
        y = i * sw + sw/2.0 + yr/2.0
        for j in range(len(data_array[0])):
            x = j * sl + sl/2.0 + xr / 2.0

            exclusion = False
            for e in exclusions:
                if e[0]-sw/2 <= x <= e[2]+sw/2 and e[1]-sw/2 <= y <= e[3]+sw/2:
                    exclusion = True

            if not exclusion:
                data_array[i, j] = Point(x, y)

            else:
                data_array[i, j] = None

    return data_array





