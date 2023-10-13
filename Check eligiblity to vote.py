#Program to check eligibility to vote - Uncle Sam

G = (raw_input("Enter 'F' if you are female, and enter 'M' if you are male:"))
A = int(raw_input("Enter your age:"))

if G == 'M' and A >= 21:
    print "Congratulations, you are eligible to vote!:)"

elif G == 'F' and A >= 18:
    print "Congratulations, you are eligible to vote!:)"

else:
    print "Sorry, you are not eligible to vote yet :("
