import time
y = "yeet"
x = "Yeet"

a = str(raw_input("Do you want to enter ?[Yeet/Nein]:"))
while (a == x)or (a== y):
        for i in range(1,6):
            print"   "*(5-i),
            for j in range (i,-i-1,-1):
                if (j == 0) or (j==-1):
                    continue
                if j in range(-1,-6,-1):
                    j = - j
                print j,
            print
        a = raw_input("Do you want to continue ?[Yeet/Nein]:")
    
