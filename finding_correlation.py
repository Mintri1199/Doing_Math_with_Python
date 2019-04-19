from matplotlib import pyplot as plt

"""
    Finding correlation
"""


def find_corr_x_y(x, y):

    n = len(x)

    # Find the sum of product
    list_of_products = []
    for xi, yi in zip(x, y):
        list_of_products.append(xi * yi)

    sum_of_prod = sum(list_of_products)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x ** 2
    squared_sum_y = sum_y ** 2

    x_square = []
    for xi in x:
        x_square.append(xi ** 2)

    # Find the sum
    x_square_sum = sum(x_square)

    y_square = []

    for yi in y:
        y_square.append(yi ** 2)

    y_square_sum = sum(y_square)

    # User formula to calculate correlation

    numerator = (n * sum_of_prod) - (sum_x * sum_y)
    denominator_term_1 = (n * x_square_sum) - squared_sum_x
    denominator_term_2 = (n * y_square_sum) - squared_sum_y
    denominator = (denominator_term_1 * denominator_term_2)**0.5

    correlation = numerator / denominator

    return correlation


def create_scatter(x, y):
    plt.scatter(x, y, marker='o')
    plt.xlabel('High School Grades')
    plt.ylabel('College Admission Test Scores')
    plt.title('Correlation between Grades and College Admission Test Scores')
    plt.show()


high_school_grades = [90, 92, 95, 96, 87, 87, 90, 95, 98, 96]

college_admission_test_scores = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]


print(find_corr_x_y(high_school_grades, college_admission_test_scores))
create_scatter(high_school_grades, college_admission_test_scores)
