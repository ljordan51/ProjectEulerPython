""" Project Euler https://projecteuler.net/archives
    Problem 1
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    Author: Lucky Jordan
    Date: 5/23/17

    All doctests will fail due to printing the runtimes.
    Want to add pickling to store known answers.
    Want to add ability to explain input to users.
"""

import sys
import time


def sumList1():
    """
    >>> sumList1()
    233168
    """
    t0 = time.time()
    numbers = [i for i in range(1, 1000)]  # creates list of all natural numbers below 1000
    multiples = [num for num in numbers if num % 3 == 0 or num % 5 == 0]  # creates list of all multiples of 3 or 5 in numbers
    ans = sum(multiples)
    t1 = time.time()
    print('sumList1: ' + str(t1-t0))
    return ans


def sumList1a():
    """
    >>> sumList1a()
    233168
    """
    t0 = time.time()
    ans = sum([num for num in range(1, 1000) if num % 3 == 0 or num % 5 == 0])  # changed to a one-liner
    t1 = time.time()
    print('sumList1a: ' + str(t1-t0))
    return ans


def sumListInputs(factors=[3, 5], upper_bound=1000):
    """
    factors = multiples of the numbers in factors will be included in the sum
    upper_bound  = maximum (not inclusive) of list of natural numbers to be filtered and summed

    >>> sumListInputs(upper_bound=10)
    23
    """
    t0 = time.time()
    multiples = []
    for num in range(1, upper_bound):
        for factor in factors:
            # add num to multiples if it is a multiple of any of the factors and has not already been added (in case it is a multiple of more than one factor)
            if num % factor == 0 and num not in multiples:
                multiples.append(num)
    ans = sum(multiples)
    t1 = time.time()
    print('sumListInputs: ' + str(t1-t0))
    return ans


def sumList2():
    """
    >>> sumList2()
    233168
    """
    t0 = time.time()
    ans = 0
    for num in range(1, 1000):
        if num % 3 == 0 or num % 5 == 0:
            ans += num  # add num to ans if its a multiple of 3 or 5
    t1 = time.time()
    print('sumList2: ' + str(t1-t0))
    return ans


if __name__ == '__main__':
    if len(sys.argv) < 2:  # if there are no input args then the doctests are run
        import doctest
        doctest.testmod(verbose=True)
    else:
        factors = [int(sys.argv[i]) for i in range(1, len(sys.argv))]  # all input args except the last are put into the list of factors as integers
        upper_bound = int(sys.argv[-1])  # last input arg is the upper bound of the series of natural numbers
        print(sumListInputs(factors, upper_bound))
