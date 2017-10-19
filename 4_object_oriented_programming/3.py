# What will be the output of the following program?
# Ans: a 
#      b
#      d
try:
    print "a"
    raise Exception("doom")
except:
    print "b"
else:
    print "c"
finally:
    print "d"
