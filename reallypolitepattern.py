import time
a = raw_input("Do you want to generate pattern ?[Yeet/Nein]:")
while (a == "Yeet") or (a=="yeet"):
    n = int(input("Enter pattern length:"))
    for k in range (1,n+1):
        
        for i in range(1,n+1):
            time.sleep(0.01)
            print"   "*(n-i),
            for j in range (i,0,-i):
                time.sleep(0.01)
                print "F",
            print
        for i in range (n,0,-1):
            time.sleep(0.01)
            print"   "*(n-i),
            for j in range (i,0,-i):
                time.sleep(0.01)
                print "F",
            print 
    a = raw_input("Do you want to continue ?[Yeet/Nein]:")

        
    if (a == "nein")or(a=="Nein"):
        print"Sorry to hear that."
        a =raw_input("Have you changed your mind ?:")
    elif (a== "yeet") or (a=="Yeet"):
        n = int(input("Enter pattern length:"))
    for k in range (1,n+1):

        for i in range(1,n+1):
            time.sleep(0.01)
            print"   "*(n-i),
            for j in range (i,0,-i):
                time.sleep(0.01)
                print "*",
            print
        for i in range (n,0,-1):
            time.sleep(0.01)
            print"   "*(n-i),
            for j in range (i,0,-i):
                time.sleep(0.01)
                print "*",
            print 
    else:
        print"Not valid input"
        a =raw_input("Have you changed your mind ?:")
