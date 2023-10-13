#Program to check the larger of two given numbers - Uncle Sam

A = float(raw_input("Enter the first number:"))
B = float(raw_input("Enter the second number:"))

if A < B:
    print B, "is larger than", A

elif A > B:
    print A, "is larger than", B

else:
    print "The two numbers are equal! HAHAHA YOU CAN'T BREAK THIS PROGRAM THAT EASILY!!!"
