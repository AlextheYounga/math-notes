import matplotlib.pyplot as plt


def graph_lines():
    x = [1, 5]
    y = [3, 10]

    # Double checking our work:
    plt.plot(x, y, label='Line')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Lines")


    #Parallel Lines
    x_parallel = [-2, 4]
    y_parallel = [8, 18.5]
    plt.plot(x_parallel, y_parallel, label='Line Parallel')

    #Perpendicular Lines
    x_perpendicular = [1, -12]
    y_perpendicular = [3, 10.428571428571427]

    plt.plot(x_perpendicular, y_perpendicular, label='Line Perpendicular')

    plt.draw()
    plt.pause(1)
    input("<Hit Enter To Close>")
    plt.close()

def graph_distance():
    point1 = (1, 3)
    point2 = (5, 10)

    x = [point1[0], point2[0]]
    y = [point1[1], point2[1]]
    plt.plot(x, y, label='Line')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Lines")

    z = (point2[0], point1[1])
    print(z)
    plt.plot(z[0], z[1], 'bo')


    plt.draw()
    plt.pause(1)
    input("<Hit Enter To Close>")
    plt.close()

graph_distance()