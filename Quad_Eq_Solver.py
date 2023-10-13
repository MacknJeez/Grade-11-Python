x = raw_input("Want to find solution of quad equation ?[Y/N]:")
while x =="Y":
    a = int(raw_input("Enter coefficient of x^2:"))
    b = int(raw_input("Enter coefficient of x:"))
    c = int(raw_input("Enter constant 'c':"))
    D = (b**2) - (4*a*c)
    if D >= 0:
        x = (-b + D**0.5)/(2*a)
        y = (-b - D**0.5)/(2*a)
        print "The solutions to the given equation are :", x, "and", y
    else :
        print "There is no rational solution to the given equation"
    x = raw_input("Continue?[Y/N]:")
