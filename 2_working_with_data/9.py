# Write a function cumulative_product to compute cumulative product of
# a list of numbers.


def cumulative_product(l):
    new_list = []
    j = 0

    for i in l:
        if len(new_list) == 0:
            new_list.append(i)
        else:
            new_list.append(new_list[j] * i)
            j += 1
    return new_list

print cumulative_product([1, 2, 3, 4])
print cumulative_product([4, 3, 2, 1])
