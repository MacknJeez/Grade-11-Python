#Find sum of digits of entered number - Uncle Sam

Number = int(raw_input("Please enter any number:"))
sum1 = 0

for A in range (1, 4):
    Remainder = Number % 10
    sum1 += Remainder
    Number = (Number - Remainder)/10

print "Sum of digits is =", sum1
