n = int(raw_input("Enter range :"))
s = 0
for i in range(0,n+1):
    fac = 1
    for j in range (0, i + 1):
        fac = fac*j
        print "Fac in loop ", i , "=", fac
    s = s + (n**i)/fac
print s
