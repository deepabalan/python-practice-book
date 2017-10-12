# Write a function factorial to compute factorial of a number. Can you
# use the product function defined in the previous example to compute
# factorial?
# factorial(4) gives 24


def factorial(num):
    if num == 1 or num == 0:
        return 1
    elif num > 1:
        return num * factorial(num - 1)

print factorial(4)
