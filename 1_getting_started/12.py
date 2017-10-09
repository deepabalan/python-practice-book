# Write a function count_digits to find number of digits in the given
# number.
# count_digits(5) = 1
# count_digits(12345) = 5


def count_digits(number):
    return len(str(number))

print count_digits(5)
print count_digits(12345)
