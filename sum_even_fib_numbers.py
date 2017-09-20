def sum():
    ls = []
    ls.append(1)
    ls.append(2)

    sum_of_even_numbers = 2
    while ls[-1] < 4000000:
        next_number = ls[-1] + ls[-2]
        ls.append(next_number)
        if next_number < 4000000 and next_number % 2 == 0:
            sum_of_even_numbers += next_number
    del ls[-1]
    return sum_of_even_numbers
print(sum())
