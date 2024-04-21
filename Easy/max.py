import itertools
import sys
from math import sqrt


def is_prime(n):
    if n <= 1:
        return False

    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i) == 0:
                return False

    return True


start_number = 100000001
for number in itertools.count(start=start_number, step=2):
    if is_prime(number):
        print(number)
        sys.exit()


def sum_primes(num):
    total = 0
    for i in range(num):
        if is_prime(i):
            total += i
    return total
    print(total)
