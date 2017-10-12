# Cumulative sum of a list [a, b, c, ...] is defined as
# [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute sum
# of a list. Does your implementation work for a list of strings?


def cumulative_sum(l):
    new_list = []
    j = 0

    for i in l:
        if len(new_list) == 0:
            new_list.append(i)
        else:
            new_list.append(new_list[j] + i)
            j += 1
    return new_list

print cumulative_sum([1, 2, 3, 4])
print cumulative_sum([4, 3, 2, 1])
print cumulative_sum(['a', 'b', 'c', 'd'])
