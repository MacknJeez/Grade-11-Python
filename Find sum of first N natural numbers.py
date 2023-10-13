#Program to find sum of first N natural numbers - Uncle Sam

#Input number of natural numbers to be added
N = int(raw_input("How many natural numbers do you want to find the sum of?"))

S = 0

#Find sum
for X in range (0, N+1):
        S += X

#Output sum
print "The sum of the first ", N, "natural numbers is = ", S
