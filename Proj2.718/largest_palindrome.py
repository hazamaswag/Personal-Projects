from math import log

def largest_palindrome(digit):
    '''
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is:
    9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

    >>> largest_palindrome(2)
    9009
    >>> largest_palindrome(3)
    906609
    '''

    i, total = 1, 0

    pal_lst = []
    i_j_pair = []
    while i < pow(10, digit):
        j = 1
        while j < pow(10, digit):
            total = i * j
            if palindrome(total):
                pal_lst += [total]
                i_j_pair += [(i,j)]
            j += 1
        i += 1
    return max(pal_lst)

def reversed(n):
    '''
    Reverses the number N.

    >>> reversed(9)
    9
    >>> reversed(1234)
    4321
    '''
    last, rest = n % 10, n // 10
    if n < 10:
        return n
    return last * (10 ** int(log(n, 10))) + reversed(rest)

    # This is a faster solution (but not by much?)
    # s = str(n)
    # rev = s[::-1]
    # return int(rev)

def palindrome(p):
    return p == reversed(p)
