import sys
import math

def factor_count(traingular_number):
    if traingular_number == 1:
        return 1
    root = int(math.sqrt(traingular_number))
    count_of_factor = 0
    for index in range(1, root + 1):
        if traingular_number % index == 0:
            # if i is a factor then n/i is also a factor
            count_of_factor += 2
    #print(count_of_factor)
    return count_of_factor


def highly_divisible_traingular_number(count_of_factor):
    traingular_number = 0
    index = 1
    while True:
        traingular_number += index
        #print(traingular_number)
        if count_of_factor <= factor_count(traingular_number):
            break;
        index += 1
    return traingular_number

if __name__ == '__main__':
    print(highly_divisible_traingular_number(int(sys.argv[1])))
