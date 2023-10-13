#Program to calculate sum of series X + X^2/2! + X^3/3! + X^4/4! + ... + X^N/N

X = int(raw_input("Enter X:"))
Y = int(raw_input("How many terms?"))

for EXP in range (1, Y + 1):

    D = 1
    N = X ** EXP

    for A in range (1, EXP + 1):

        D *= A

    S = N / D
    S += S

print S
