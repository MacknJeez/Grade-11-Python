import random
a = raw_input
while a == "Y":
    n = int(raw_input("Enter:"))
    m = int(raw_input("Enter:"))
    n = n*10.0
    m = m*10.0
    x = random.randrange(n,m)
    print x/10.0
    a = raw_input("Continue?[Y/N]:")
