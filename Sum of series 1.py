#Find sum of series 1 + 2x^2 + 3x^3 + ... + nx^n

X = int(raw_input("What should be the coefficient of X?"))
N = int(raw_input("How many terms do you want?"))
lad = 0

for N in range (2, N + 1):
    N += 1

lad = N * (X ** N)

print "The sum of the series is ", lad + 1
