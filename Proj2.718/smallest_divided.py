def smallest_divided(start, end):
    '''
    2520 is the smallest number that can be divided by each of the numbers from:
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers
    from 1 to 20?

    >>> smallest_divided(1, 10)
    2520
    >>> smallest_divided(1, 20)
    232792560
    >>> smallest_divided(1, 30)
    2329089562800
    '''

    og_start, i = start, 2
    while start <= end:
        if i % start == 0:
            start += 1
            if start > end:
                return i
        else:
            start = og_start
            i += 1

# This is MUCH faster and it uses Euler's method for calculating GCD
# def gcd(a, b):
#     while(a > 0 and b > 0):
#         if (a > b):
#             a = a % b
#         else:
#             b = b % a
#     return a + b
#
# def lcm(a, b):
#     return ((a * b) / (gcd(a, b)))
#
# i = 1
# mult = 1
# while (i <= 20):
#      mult = lcm(i, mult)
#      i += 1
#
# print(mult)
