
week = 0
days = int(raw_input("Enter first day of year[Sunday= 1,Monday=2,Tuesday=3.......]:"))
if days > 7:
    print "Invalid Day"
    days = int(raw_input("Enter first day of year[Sunday= 1,Monday=2,Tuesday=3.......]:"))    
n = int(raw_input("Enter day number required:"))
for i in range (1,n+1):
    days =days +1
    if days > 7:
        days= 1
        week = week +1
    print days , week 

print (days-1)

