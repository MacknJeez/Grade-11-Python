x = int(raw_input("Enter 1st Military format time:"))
y = int(raw_input("Enter 2nd Military format time:"))
if x > y :
    a = x-y
elif y >x:
    a = y-x
b = a%100
c = a - b
d = (c/100)
if b >60:
    d = d +1
    b = b - 60
print d, " Hours", b," Minutes"
