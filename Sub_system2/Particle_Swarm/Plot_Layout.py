import matplotlib.pyplot as plt


def plot_layout(x, y, source, length, width):

    fig1 = plt.figure()

    plt.axis([0, length, 0, width])
    ax2 = fig1.add_subplot(1, 1, 1)

    rect1 = plt.Rectangle((3.2, 0), 1, 3)
    rect2 = plt.Rectangle((3.2, 10.59), 1, 3)
    rect3 = plt.Rectangle((6.9, 0), 1, 3)
    rect4 = plt.Rectangle((6.9, 10.59), 1, 3)
    rect5 = plt.Rectangle((10.6, 0), 1, 3)
    rect6 = plt.Rectangle((10.6, 10.59), 1, 3)
    rect7 = plt.Rectangle((0, 10.59), 15.084, 0.5)
    rect8 = plt.Rectangle((0, 3), 15.084, 0.5)

    ax2.add_patch(rect1)
    ax2.add_patch(rect2)
    ax2.add_patch(rect3)
    ax2.add_patch(rect4)
    ax2.add_patch(rect5)
    ax2.add_patch(rect6)
    ax2.add_patch(rect7)
    ax2.add_patch(rect8)

    plt.plot(x, y, 'ro')
    plt.plot(source[0], source[1], 'go')

    plt.show()
