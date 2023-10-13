a = raw_input("Do you want to generate pattern ?[Yeet/Nein]:")
while (a == "Yeet") or (a=="yeet"):

        n = int(raw_input("Enter range:"))
        for k in range(1,n+1):
            for i in range(1,n+1):
                print "   "*(n-i),
                for j in range(i,0,-1):
                    print j,
                print 
            for i in range(n,0,-1):
                print "   "*(n-i),
                for j in range(1,i+1):
                    print j,
                print 
        if (a == "nein")or(a=="Nein"):
            print"Sorry to hear that."
            a =raw_input("Have you changed your mind ?:")
        else:
            print"Not valid input"
            a =raw_input("Have you changed your mind ?:")
