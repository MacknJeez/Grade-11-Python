#Program to generate multiples of any number, any number of times - Uncle Sam

ZOIN = 69
while ZOIN == 69:
    X = int(raw_input("Enter number:"))
    Y = int(raw_input("Enter number of multiples required:"))

    for A in range (1,Y+1):
        print X, "X ", A, "=", X*A

    print "More?????"
    ZEE = int(raw_input("Input 0 to stop, 1 to continue:"))

    if ZEE == 0:
        print "bye m8"

    else:
        X = int(raw_input("Enter number:"))
        Y = int(raw_input("Enter number of multiples required:"))

        for A in range (1,Y+1):
            print X, "X ", A, "=", X*A

    
