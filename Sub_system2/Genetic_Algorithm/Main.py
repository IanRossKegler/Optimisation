from Plot_Layout import plot_layout
from Point import Point
import random
from Args import size_of_population, best_sample, lucky_few, chair_rad, \
    width, length, source, exclusions, spl1, r1, c20, min_spl, generations
import time
start = time.time()


def valid_point(population, point, source, chair_rad, exclusions, min_spl, spl1, r1):

    xs, ys = source
    con1 = False
    con2 = False
    con3 = True
    con4 = True

    if point.direct_l(xs, ys) > r1:
        con1 = True

    if point.spl_direct(spl1, r1, xs, ys) > min_spl:
        con2 = True

    for e in exclusions:
        if e[0] - chair_rad <= point.x <= e[2] + chair_rad and e[1] - chair_rad <= point.y <= e[3] + chair_rad:
            con3 = False

    if len(population) > 0:
        for p in population:
            if point.direct_l(p.x, p.y) < 2 * chair_rad:
                con4 = False

    if con1 and con2 and con3 and con4:
        return True

    else:
        return False

def population_fitness (population, source, width, length, c20):

    xs, ys = source

    for p in population:
        p.ave_dt(xs, ys, width, length, c20)

    return population

def generate_point(chair_rad, width, length):

    x = chair_rad + random.random() * (length - 2 * chair_rad)
    y = chair_rad + random.random() * (width - 2 * chair_rad)
    point = Point(x, y)
    return point

def generate_first_population(size_population, chair_rad, width, length, source, exclusions, min_spl, spl1, r1):

    population = []
    i = 0

    while i < size_population:

        point = generate_point(chair_rad, width, length)

        if valid_point(population, point, source, chair_rad, exclusions, min_spl, spl1, r1):
            population.append(point)
            i += 1

        else:
            pass
    return population

def select_from_population(population, source, chair_rad, exclusions, width, best_sample, lucky_few):

    next_generation = []
    population = population_fitness(population, source, chair_rad, exclusions, width)
    population_sorted = sorted(population, key=lambda point: point.ave_dt)

    for i in range(best_sample):
        next_generation.append(population_sorted[i])
        del population_sorted[i]
    for i in range(lucky_few):
        next_generation.append(random.choice(population_sorted))

    random.shuffle(next_generation)
    return next_generation

def create_child(var1, var2):

    x1 = var1.x
    y1 = var1.y
    x2 = var2.x
    y2 = var2.y

    x1_bin_str = str(bin(int(x1 * 100)))
    y1_bin_str = str(bin(int(y1 * 100)))
    x2_bin_str = str(bin(int(x2 * 100)))
    y2_bin_str = str(bin(int(y2 * 100)))

    while len(x1_bin_str) < 14:
        x1_bin_str = x1_bin_str[:2] + '0' + x1_bin_str[2:]

    while len(y1_bin_str) < 14:
        y1_bin_str = y1_bin_str[:2] + '0' + y1_bin_str[2:]

    while len(x2_bin_str) < 14:
        x2_bin_str = x2_bin_str[:2] + '0' + x2_bin_str[2:]

    while len(y2_bin_str) < 14:
        y2_bin_str = y2_bin_str[:2] + '0' + y2_bin_str[2:]

    child_x_bin_str = ''
    child_y_bin_str = ''

    for i in range(len(x1_bin_str)):
        if int(100 * random.random()) < 50:
            child_x_bin_str += x1_bin_str[i]
        else:
            child_x_bin_str += x2_bin_str[i]

    for i in range(len(y1_bin_str)):
        if int(100 * random.random()) < 50:
            child_y_bin_str += y1_bin_str[i]
        else:
            child_y_bin_str += y2_bin_str[i]

    child = Point(eval(child_x_bin_str)/100, eval(child_y_bin_str)/100)
    return child

def create_children(population, source, chair_rad, exclusions, min_spl, spl1, r1):
    next_population = []

    population1 = population.copy()
    population2 = population.copy()

    for i in range(len(population)):

        valid = False

        i1 = random.randint(0, len(population1)-1)
        i2 = random.randint(0, len(population2)-1)

        parent1 = population1[i1]
        parent2 = population2[i2]

        while not valid:

            child = create_child(parent1, parent2)

            if valid_point(next_population, child, source, chair_rad, exclusions, min_spl, spl1, r1):
                next_population.append(child)
                del population1[i1]
                del population2[i2]
                valid = True
    return next_population

def multiple_generation(number_of_generations, size_population, chair_rad, width, length, source, exclusions, min_spl, spl1, r1):

    historic = []

    historic.append(generate_first_population(size_population, chair_rad, width, length, source, exclusions, min_spl, spl1, r1))

    for i in range(number_of_generations):
        historic.append(create_children(historic[i], source, chair_rad, exclusions, min_spl, spl1, r1))
    return historic


layout = multiple_generation(generations, size_of_population, chair_rad, width, length, source, exclusions, min_spl, spl1, r1)

print('layout size = ' + str(len(layout[-1])))
print('runtime = ' + str(time.time()-start))
plot_layout(layout[-1], source, length, width)



