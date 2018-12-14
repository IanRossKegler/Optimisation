from scipy.optimize import minimize
from Innit_Array import init_array
from Args import width, length, chair_width, chair_length, exclusions, func_args, x0
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

                p.spl(L1, r1, x0, y0, length, width)
                d = p.direct_l(x0, y0)
                spl = p.spl_direct

                p.calc_error(des)

                if spl >= min_spl and d >= r1:
                    points.append(p)

    sorted_points = sorted(points, key=lambda point: point.error)  # sort by ave_dt
    sorted_points = sorted_points[0:n]

    for p in sorted_points:
        x.append(p.x)
        y.append(p.y)
        sorted_ave_dt.append(p.ave_dt)

    layout_ave_dt = sum(sorted_ave_dt) / len(sorted_ave_dt)

    return layout_ave_dt


def exclusion_constraints(S, *args):
    xs, ys = S
    width, length, c20, L1, r1, min_spl, n, des, exclusions, sw, sl = args

    exclusion = 1
    for e in exclusions:
        if e[0] - sw / 2 <= xs <= e[2] + sw / 2 and e[1] - sw / 2 <= ys <= e[3] + sw / 2:
            exclusion = -1

    return exclusion

def geometric_constraints(S, *args):
    xs, ys = S
    width, length, c20, L1, r1, min_spl, n, des, exclusions, sw, sl = args

    bounded = -1

    bounds = [0, length, 0, width]

    if bounds[0] <= xs <= bounds[1] + sw / 2 and bounds[2] - sw / 2 <= ys <= bounds[3] + sw / 2:
        bounded = 1

    return bounded


point_array = init_array(width, length, chair_width, chair_length, exclusions)
con = [{'type': 'ineq', 'fun': exclusion_constraints, 'args': func_args},
       {'type': 'ineq', 'fun': geometric_constraints, 'args': func_args}]

x = []
y = []

res = minimize(layout_ave_delay, x0, func_args,  method='COBYLA', constraints=con,
               options={'rhobeg': 1.0, 'maxiter': 1000, 'disp': False, 'catol': 0.0002})

print(res.x)
print(len(x))
print(time.time()-start)
plot_layout(x, y, res.x, length, width)
