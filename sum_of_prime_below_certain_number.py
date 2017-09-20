import prime_number_checker as pnc
import sys
import time
def sum_of_prime_numbers_below_n(upper_limit):
    current_number = 2
    sum = 0
    while True:
        if pnc.isPrime(current_number) and current_number < upper_limit:
            sum += current_number
        elif current_number >= upper_limit:
            break
        current_number += 1

    return sum

if __name__ == '__main__':
    start_time = time.time()
    print(sum_of_prime_numbers_below_n(int(sys.argv[1])))
    print('Total seconds to execute', time.time() - start_time)
