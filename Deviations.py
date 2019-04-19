"""
    Find the standard and variance deviation
"""

from matplotlib import pyplot as plt


def draw_graph(x, y, marker=bool):
    if marker:
        plt.plot(x, y, marker="o")
    else:
        plt.plot(x, y)

    plt.xlabel("Numbers of days")
    plt.ylabel("Value of donations")
    plt.title('Variance and deviation of donations')


def calculate_mean(numbers):

    s = sum(numbers)
    n = len(numbers)

    mean = s/n

    return mean


def find_difference(numbers):
    # Find the mean
    mean = calculate_mean(numbers)

    # Find the differences from the mean
    diff = []

    for num in numbers:
        diff.append(num - mean)

    return diff


def calculate_variance(numbers):

    # Find the list of differences
    diff = find_difference(numbers)

    # Find the squared differences
    square_diff = []
    list_of_variances = []
    list_of_standard_deviation = []
    for d in diff:
        square_diff.append(d**2)

    # sum_square_diff = sum(square_diff)
    # variance = sum_square_diff/len(square_diff)
    # list_of_variances.append(variance)
    # list_of_standard_deviation.append(variance**0.5)

    # Find the variances
    sum_square_diff = sum(square_diff)
    variance = sum_square_diff/len(numbers)

    return variance  #, list_of_variances, list_of_standard_deviation


if __name__ == "__main__":
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    # donation_2 = [382, 389, 377, 397, 396, 368, 369, 392, 398, 367, 393, 396]
    days = range(0, len(donations))
    # variance, list_of_variances, std = calculate_variance(donations)
    variance = calculate_variance(donations)
    print('The variance of the list of numbers is {0}'.format(variance))

    std = variance ** 0.5
    print('The standard deviation of the list of numbers is {0}'.format(std))

# # Drawing the mean line
    # mean_list = []
    #
    # for i in days:
    #     mean_list.append(calculate_mean(donations))
    #
    # draw_graph(days, mean_list, False)
    #
    # # Drawing the donations get
    # draw_graph(days, donations, True)
    #
    # # Draw the standard deviation
    # draw_graph(days, std, True)
    # print(std)
    # # Draw the variation
    # draw_graph(days, list_of_variances, True)
    # std = variance**0.5
    #
    # plt.legend(['Mean', 'Donations', "Standard Deviation", "Variance"])
    #
    # plt.show()
