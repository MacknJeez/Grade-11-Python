x = int(raw_input("Enter 1st Military format time:"))
y = int(raw_input("Enter 2nd Military format time:"))
if x > y :
    b= x-y
elif y >x:
    b= y-x
elif y == x:
    b = x - y
c= b%100
d = b- c
e = (d/100)
if c >60:
    e = e +1
    c = c - 60
print e, " Hours", c," Minutes"
