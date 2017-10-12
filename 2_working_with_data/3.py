# What happens when the above sum function is called with a list of
# strings? Can you make your sum function work for a list of strings
# as well.
# sum(["hello", "world"]) gives "helloworld"
# sum(["aa", "bb", "cc"])


def str_list_sum(t):
    tot = ''
    for i in t:
        tot += i
    return tot    

print str_list_sum(["hello", "world"])
print str_list_sum(["aa", "bb", "cc"])
