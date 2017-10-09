# Write a function istrcmp to compare two strings, ignoring the case.
# istrcmp('python', 'Python') True
# istrcmp('LaTeX', 'Latex') True
# istrcmp('a', 'b') False


def istrcmp(str1, str2):
    return str1.lower() == str2.lower()

print istrcmp('python', 'Python')
print istrcmp('LaTeX', 'Latex')
print istrcmp('a', 'b')
