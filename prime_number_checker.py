import math
import sys
def isPrime(number):
    sqr_root = int(math.sqrt(number))
    is_prime = True
    for count in range(2, sqr_root + 1):
        if number % count == 0:
            is_prime = False
            break

    return is_prime
