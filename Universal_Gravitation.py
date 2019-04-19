import matplotlib.pyplot as plt


def create_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitational force and distance')
    plt.show()


def generate_f_r():
    # Generate value for r
    r = range(100, 1001, 50)
    # Empty list to store calculated values for f
    F = []

    # Constant of G
    G = 6.674*(10**-11)
    # Two  masses
    m1 = 0.5
    m2 = 1.5

    # Calculate the force and add it to the list, F
    for dist in r:
        force = G*(m1*m2)/(dist**2)
        F.append(force)

    # Call draw graph function
    create_graph(r, F)


if __name__ == '__main__':
    generate_f_r()


