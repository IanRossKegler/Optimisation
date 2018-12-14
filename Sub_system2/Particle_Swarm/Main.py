from pyswarm import pso
from Innit_Array import init_array
from Args import func_args, width, length, chair_length, chair_width, exclusions, ub, lb, l1, r1, min_spl
from Plot_Layout import plot_layout
import time
start = time.time()

def layout_ave_delay(S, *args):
    global point_array
    global x
    global y

    x0, y0 = S
    width, length, c20, L1, r1, min_spl, n, des, exclusions, sw, sl = args

    points = []
    sorted_ave_dt = []
    x = []
    y = []

    for i in range(len(point_array[:, 0])):
        for j in range(len(point_array[0])):
            p = point_array[i, j]

            if p is not None:

                ave_pl = p.ave_pl(x0, y0, width, length)
                ave_dif_dist = ave_pl - p.direct_l(x0, y0)
                p.ave_dt = ave_dif_dist / c20

                p.spl(L1, r1, x0, y0)
                d = p.direct_l(x0, y0)
                spl = p.spl_direct

                p.calc_error(des)

                if spl >= min_spl and d >= r1:
                    points.append(p)

    sorted_points = sorted(points, key=lambda point: point.error)   # sort by ave_dt
    sorted_points = sorted_points[0:n]

    for p in sorted_points:
        x.append(p.x)
        y.append(p.y)
        sorted_ave_dt.append(p.ave_dt)

    layout_ave_dt = sum(sorted_ave_dt)/len(sorted_ave_dt)

    return layout_ave_dt


def geometric_constraints(S, *args):
    xs, ys = S
    width, length, c20, L1, r1, min_spl, n, des, exclusions, sw, sl = args

    exclusion = 1
    for e in exclusions:
        if e[0] - sw / 2 <= xs <= e[2] + sw / 2 and e[1] - sw / 2 <= ys <= e[3] + sw / 2:
            exclusion = -1

    return exclusion


point_array = init_array(width, length, chair_width, chair_length, exclusions)
x = []
y = []

xopt, fopt = pso(layout_ave_delay, lb, ub, f_ieqcons=geometric_constraints, args=func_args)

print('source = ' + str(xopt))
print('layout average delay = ' + str(fopt))
print('runtime = ' + str(time.time()-start))

plot_layout(x, y, xopt, length, width)

