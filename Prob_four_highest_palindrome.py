import sys

def highest_palindrome():
    palindrom = 0
    for c1 in range(100, 999):
        for c2 in range(100, 999):
            tmp_number = c1 * c2
            tmp_number_str = str(tmp_number)
            if "".join(reversed(tmp_number_str)) == tmp_number_str and tmp_number > palindrom:
                palindrom = tmp_number
                print(palindrom)

if __name__ == '__main__':
    highest_palindrome()
