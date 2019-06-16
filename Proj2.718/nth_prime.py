def nth_prime(n):
    '''
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    >>> nth_prime(1)
    2
    >>> nth_prime(6)
    13
    >>> nth_prime(10 001)
    104743
    '''

    pp = 2
    ps = [pp]
    while pp < n:
        pp += 1
        for a in ps:
            if a*a > pp:         # stop
                ps.append(pp)    #  early
                break
            if pp%a==0:
                break

    return ps[10001-1]
