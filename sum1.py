#This is for inputing the number
x = int(raw_input("Enter number:"))
y = str(raw_input("Do you want to ?:"))
while y == "Y":
    if x == 0:
        print"Zero"
    elif x == 1:
        print"One"
    elif x == 2:
        print"Two"
    elif x == 3:
        print "Three"
    elif x == 4:
        print"Four"
    elif x == 5:
        print"Five"
    elif x == 6:
        print"Six"
    elif x == 7:
        print "Seven"
    elif x == 8:
        print"Eight"
    elif x == 9:
        print"Nine"
    y = str(raw_input("Do you want to continue[Y/N]?:"))
    x = int(raw_input("Enter number:"))
#I had put if instead of elif, I have corrected it.
    
