# Write a function dups to find all duplicates in the list.


def dups(l):
    unique = []
    dup_list = []
    for i in l:
        if i not in unique:
            unique.append(i)
        else:
            dup_list.append(i)
    return dup_list

print dups([1, 2, 1, 3, 2, 5])
