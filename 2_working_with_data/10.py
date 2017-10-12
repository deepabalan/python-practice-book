# Write a function unique to find all the unique elements of a list.


def unique(l):
    new_list = []
    for i in l:
        if i not in new_list:
            new_list.append(i)
    return new_list

print unique([1, 2, 1, 3, 2, 5])
