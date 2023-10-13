# To find sum of series ( 1 + 2x^2 + 3x^3 + ..... + Nx^N)
a = str(raw_input("Do you want to find sum of first n numbers?[Y/N]:"))
while a == "Y":
    x = int(raw_input("Enter x"))
    b = int(raw_input("Enter n"))
    for c in range (1,b+1):
        s = c*(c**x) + 1
    print s 
    raw_input("Do you want to continue ?[Y/N]:")
