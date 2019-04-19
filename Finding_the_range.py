'''
    Find the range
'''

def find_range(numbers):

    lowest = min(numbers)
    highest = max(numbers)

    r = highest - lowest

    return highest, lowest, r


if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]

    highest, lowest, r = find_range(donations)
    print('Lowest: {0} Highest: {1} Range: {2}'.format(lowest, highest, r))