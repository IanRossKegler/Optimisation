exclusions = [[3.2, 0, 4.2, 3], [3.2, 10.59, 4.2, 13.59], [6.9, 0, 7.9, 13.59],
              [6.9, 10.59, 7.9, 13.59], [10.6, 0, 11.6, 3], [10.6, 10.59, 11.6, 13.59], [0, 10.09, 15.084, 10.59],
              [0, 3, 15.084, 3.5]]  # rectangular exclusion zones [x0, y0, x1, y1]

width = 13.59
length = 15.084

chair_width = 0.8
chair_length = 0.8

L1 = 80                     # Sound Pressure Level in dB at 1m
r1 = 1                      # distance from source of measured L1
c20 = 343                   # speed of sound in air (m/s)
min_spl = 50                # minimum sound pressure level
n = 61                      # number of chairs
des = 0                     # desired delay

array_args = (width, length, chair_width, chair_length, exclusions)
func_args = (width, length, c20, L1, r1, min_spl, n, des, exclusions, chair_width, chair_length)

x0 = (length/2, width/2)
