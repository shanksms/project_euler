import math
import sys
import prime_number_checker as pnc
#logic to find out nth prime number

def findNthPrimeNumber(n):
    prime_number_counter = 0
    current_number = 2
    current_prime_number = None
    while True:
        if pnc.isPrime(current_number):
            current_prime_number = current_number
            prime_number_counter += 1
            if prime_number_counter == n:
                break

        current_number += 1
    return current_prime_number
if __name__ == '__main__':
    n = int(sys.argv[1])
    print(findNthPrimeNumber(n))
