#You that this program would find you a date? Ha. This a program , not magic.
week = 0
a = raw_input("Run Prog?[Y/N]:")
while a =="Y":
    days = int(raw_input("Enter first day of year[Sunday= 1,Monday=2,Tuesday=3.......]:"))
    n = int(raw_input("Enter day number required:"))
    for i in range (1,n+1):
        days =days +1
        if days > 7:
            days= 1
            week = week +1
    if (days-1) == 1:
        print "Sunday",
    elif (days-1) == 2:
        print "Monday",
    elif (days-1)== 3 :
        print "Tuesday",
    elif (days-1)== 4:
        print "Wednesday",
    elif (days-1)== 5:
        print"Thursday",
    elif (days-1) == 6:
        print "Friday",
    elif (days-1)== 7:
        print "Saturday",
    print "Week ",week


    a = raw_input("ReRun Prog ?[Y/N]:")
