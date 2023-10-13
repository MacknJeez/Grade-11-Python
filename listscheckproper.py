l1=[]
abc = 0
x = int(raw_input("How many terms ?:"))
for i in range(0,x):
    askterms = raw_input("Enter term {}/{}:".format(i,x))
    l1.extend(askterms)
print l1
for j in range(0,len(l1)):
    if l1[j] == True:
        abc = abc +1
    print abc 
    
    
