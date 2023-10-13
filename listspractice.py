def GetPosAndModify():
    abc = 0
    random = 0
    for j in range(0,len(l1)-1):
            if modifyask == l1[j]:
                l1.pop(j)
                insertnew= raw_input("What do you want to input in its place ?:")
                l1.insert(j,insertnew)
                l1[j] = int(l1[j])
def Remove():
    random = 0
    for k in range(0,len(l1)-1):
            if removeask == l1[k]:
                l1.pop(k)
def GetPosAndInsert():
        for l in range(0,len(l1)-1):
            if insertask == l1[l]:
                insertnew2= int(raw_input("What do you want to input after {} ?:".format(insertask)))
                l1.insert(l+1,insertnew2)
def Check():
    abc = 0 
    for m in range(0,len(l1)-1):
        if checkask == l1[m]:
            abc = abc+1
        elif checkask != l1[m]:
            abc = 0 
        print " The number {} repeats  {} times in the list".format(checkask,abc)



l1= []
a = int(raw_input("How many terms ?:"))
for i in range(0,a):
    b = int(raw_input("Enter term {}:".format(i)))
    l1.insert(i,b)
print l1
while True:
    print """Modify
Remove
Insert
Check for repeats"""
    ask= raw_input("What do you want to do to the list ?(Case Sensitive):")
    if ask == "Modify":
        modifyask= int(raw_input("What element do you want to modify ?:"))
        GetPos()
        print l1
    elif ask == "Remove":
        removeask= int(raw_input("What element you wanna remove ?:"))
        Remove()
        print l1
    elif ask =="Insert":
        insertask= int(raw_input("After what element you wanna enter ?:"))
        GetPosAndInsert()
        print l1
    elif ask == "Check" or ask == "Check for repeats" :
        checkask = int(raw_input("Which number you wanna check for?:"))
        Check()
        print l1
    else :
        print "Invalid"
        exit()
    
