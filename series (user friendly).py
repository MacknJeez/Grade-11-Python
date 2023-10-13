# To find sum of series ( 1 + 2x^2 + 3x^3 + ..... + Nx^N)
a = str(raw_input("Do you want to find sum of first n numbers?[Y/N]:"))
while a == "Y":
    s = 0
    x = int(raw_input("Enter x"))
    n = int(raw_input("Enter n"))
    for i in range (2,n+1):
        s = i*(x**i) + s
    
    print s +1 
    raw_input("Do you want to continue ?[Y/N]:")
