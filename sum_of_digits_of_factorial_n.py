import sys
import factorial

def total_sum(n):
    return sum([int(i) for i in str(n)])

if __name__ == '__main__':
    input_number = int(sys.argv[1])
    print(total_sum(factorial.factorial(input_number)))
