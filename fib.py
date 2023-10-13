n = int(raw_input("Enter range:"))
#0,1,1,2,3,5,8,13......
a = 0
b = 1
print a
print b
for i in range (1,n+1):
    c = a +b
    a,b=b,c
    print c
