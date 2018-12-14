size_of_population = 35
best_sample = 30
lucky_few = 5
no_of_children = 2
chair_rad = 0.5
width = 13.59
length = 15.084
source = [3, width/2]
exclusions = [[3.2, 0, 4.2, 3], [3.2, 10.59, 4.2, 13.59], [6.9, 0, 7.9, 13.59],
              [6.9, 10.59, 7.9, 13.59], [10.6, 0, 11.6, 3], [10.6, 10.59, 11.6, 13.59], [0, 10.59, 15.084, 10.59],
              [0, 3, 15.084, 3.5]]  # rectangular exclusion zones [x0, y0, x1, y1]min_spl
spl1 = 85
r1 = 1
c20 = 344
min_spl = 0
generations = 1

kwargs = {"best_sample":best_sample, "lucky_few":lucky_few, "no_of_children":no_of_children, "chair_rad":chair_rad,
          "width":width, "length":length, "source":source, "exclusions":exclusions, "spl1":spl1, "r1":r1, "c20":c20,
          "size_of_population":size_of_population}

args = [size_of_population, best_sample, lucky_few, no_of_children, chair_rad, width, length, source, exclusions, spl1, r1, c20]
