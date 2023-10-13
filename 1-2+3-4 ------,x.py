n = int(raw_input("Enter range:"))
s = 0
for i in range(1,n+1):
    if (i%2) == 0:
        i = -i
    elif (i%2) == 1:
        i = i
    s = s + i
print s
