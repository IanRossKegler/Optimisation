import numpy as np

class Point:
    def __init__(self, x, y, ave_dt=None, spl_dir=None):
        self.x = x
        self.y = y
        self.ave_dt = ave_dt
        self.spl_dir = spl_dir

    def direct_l(self, x0, y0):
        d = np.sqrt((self.x - x0)**2 + (self.y - y0)**2)
        return d

    def first_a(self, x0, y0):
        h1 = (abs(self.y - y0)*(1 - 1/(self.x/x0 + 1)))
        h2 = (abs(self.y - y0)/(self.x/x0 + 1))
        pl = np.sqrt((h1**2 + self.x**2)) + np.sqrt((h2**2 + x0**2))
        return pl

    def first_b(self, x0, y0, w):
        h1 = (abs(self.x - x0)*(1 - 1/((w - y0)/(w - self.y) + 1)))
        h2 = (abs(self.x - x0)/((w - y0)/(w - self.y) + 1))
        pl = np.sqrt((h1**2 + (w - y0)**2)) + np.sqrt((h2**2 + (w - self.y)**2))
        return pl

    def first_c(self, x0, y0, l):
        h1 = (abs(self.y - y0) * (1 - 1 / ((l - self.x) / (l - x0) + 1)))
        h2 = (abs(self.y - y0) / ((l - self.x) / (l - x0) + 1))
        pl = np.sqrt((h1**2 + (l - self.x)**2)) + np.sqrt((h2**2 + (l - x0)**2))
        return pl

    def first_d(self, x0, y0):
        h1 = (abs(self.x - x0) * (1 - 1 / (y0 / self.y + 1)))
        h2 = (abs(self.x - x0) / (y0 / self.y + 1))
        pl = np.sqrt((h1**2 + y0**2)) + np.sqrt(h2**2 + self.y**2)
        return pl

    def ave_dt(self, x0, y0, l, w, c):
        d1 = self.first_a(x0, y0)
        d2 = self.first_b(x0, y0, w)
        d3 = self.first_c(x0, y0, l)
        d4 = self.first_d(x0, y0)
        ave = (d1 + d2 + d3 + d4)/4
        ave_dt = ave/c
        self.ave_dt = ave_dt
        return ave_dt

    def spl_direct(self, l1, r1, x0, y0):
        r2 = self.direct_l(x0, y0)
        spl_direct = l1 - abs(20*np.log(r1/r2))
        self.spl_dir = spl_direct
        return spl_direct
