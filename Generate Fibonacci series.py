#Program to generate Fibonacci series

Z = int(raw_input("How many numbers do you want in the series?"))
A = 0
B = 1

print "Series:"
print 0
print 1

#Generate series
for lad in range (1, Z - 1):

    C = A + B
    A = B
    B = C

    print C
