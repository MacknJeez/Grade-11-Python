a = str(raw_input("Do you want to ?[Y/N]:"))
x = int(raw_input("Enter variable :"))
n = int(raw_input("Enter range :")) 
s = 0
while a == "Y":

    for i in range(1,n+1):
        fac = 1
        for j in range (1,i+1):
            fac = fac*j
            print "Factorial in loop ", i , "=", fac
        s = s + (x**i)/fac
    print s

    a = str(raw_input("Do you want to continue?[Y/N]:"))
    x = int(raw_input("Enter variable :"))
    n = int(raw_input("Enter range :"))
