#Program to generate multiples of 2, 3, 4, and 5 - Uncle Sam

A = 2

while A < 6:
    B = 1

    while B < 11: 
        print A, "X", B, "=", A * B
        B += 1

    A += 1

print 'That\'s it mate'
