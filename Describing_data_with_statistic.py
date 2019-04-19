'''
    Calculating the median 
'''


# The parameter accept a list of numbers (doesn't need to be sorted)
def calculate_median(numbers):

    N = len(numbers)  # N is the size of the list of numbers
    numbers.sort()

    # Find the median
    if N % 2 ==  0:
        # if N is even
        m1 = N/2
        m2 = (N/2) + 1

        # convert to integers
        m1 = int(m1) - 1
        m2 = int(m2) - 1

        median = (numbers[m1] + numbers[m2])/2

    else:
        m = (N+1)/2
        m = int(m)

        median = numbers[m]

    return median


if __name__ == "__main__":
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    print(calculate_median(donations))