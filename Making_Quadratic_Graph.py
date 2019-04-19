from matplotlib import pyplot as plt


# Give list of x values in the parameter
def calculate(x):

    y_values = []

    for i in x:
        y = i**2 + 2*i - 1
        y_values.append(y)

    return y_values


# Draw the graph with the two lists of x and y values
def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel("X values")
    plt.ylabel('Y values')
    plt.title('Quadratic roots')


if __name__ == "__main__":
    x_list = range(-100, 100)
    y_list = calculate(x_list)

    draw_graph(x_list, y_list)

    plt.show()