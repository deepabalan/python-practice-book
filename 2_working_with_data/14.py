# Improve the unique function written in previous problems to take an
# optional key function as argument and use the return value of the
# key function to check for uniqueness.


def unique(l, key):
    t = []
    for i in [key(i) for i in l]:
        if i not in t:
            t.append(i)
    return t

print unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
