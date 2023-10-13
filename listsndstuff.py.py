l1=[]
a = int(raw_input("how many terms?:"))
while True:
    for i in range(0,a):
        b = int(raw_input("Enter term {}:".format(i)))
        l1.insert(i,b)
    print l1
    c = raw_input("Want to modify ?:[Y/N]")
    if c == "Y":
        print l1
        d = int(raw_input("Which element do you want to change ?:"))
        for j in range(0,len(l1)):
            if j == d:
                l1.pop(j)
        e = int(raw_input("Enter New value:"))
        l1.insert(d,e)
        print l1
        
