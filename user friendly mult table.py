a = int(raw_input("Enter multiplication table of :"))
n =  int(raw_input("Enter up until which number :"))
c = 0
b = 0
d = 
while d != 0:
    while c in range(n + 1) :
        print 'Table of ', n , 'is',
        for b in range (0,13):
            print c , 'x', b,'=', c*b
        c = c+1
        
    
