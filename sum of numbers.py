n = int(raw_input("Enter number of digits:"))
Number = int(raw_input("Enter number :"))
sum1 = 0

for n in range(1,n+1):
    remainder = Number % 10
    sum1 = remainder + sum1

    print "The sum of numbers is ;" , sum1
    
