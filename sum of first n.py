#To find sum of first n numbers
a = raw_input("do you want to find the sum of first n numbers ?[Y/N]:")
d = 0
while a =="Y":
    b = int(raw_input("Enter n:"))
    for c in range(1,b+1):
        d = c + d    
    print "The sum of first " , b, "numbers is :" , d
    raw_input("Do you want to continue ?[Y/N]:")
