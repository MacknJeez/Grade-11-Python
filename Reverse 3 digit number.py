#Program to reverse 3 digits - Uncle Sam

A = int(raw_input("Enter number:"))
X = 0

for X in range (1, 4):
    R = A % 10
    A = (A - R) / 10

    print R
