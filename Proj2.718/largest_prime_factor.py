from math import sqrt

def largest_prime_factor(n):
    '''
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?

    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(21)
    7
    >>> largest_prime_factor(48)
    3
    >>> largest_prime_factor(600851475143)
    6857
    '''
    # original somewhat failed solution
    # i, lst_primes = 2, []
    # while i*i <= n:
    #     if n % i == 0:
    #         lst_primes += [i]
    #     i += 1
    #
    # return lst_primes

    i = 2
    while n > 1:
	       if n % i == 0:
		       n /= i
	       else:
		       i += 1
    return i
