def sum_square_difference(n):
    '''
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first
    ten natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the
    first one hundred natural numbers and the square of the sum.

    >>> sum_square_difference(10)
    2640
    >>> sum_square_difference(100)
    25164150
    '''

    return square_sum(n) - sum_square(n)

def sum_square(n):
    '''
    Calculates the sum of the squares of the first N numbers

    >>> sum_square(10)
    385
    '''
    total = 0
    while n:
        total += n ** 2
        n -= 1
    return total

def square_sum(n):
    '''
    Calculates the sqaures of the first N numbers then sums them

    >>> square_sum(10)
    3025
    '''
    total = 0
    while n:
        total += n
        n -= 1
    return total ** 2
