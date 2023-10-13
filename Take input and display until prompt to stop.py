#Program to take input and display it until user prompts to stop - Uncle Sam

x = 0

while x == 0:

    A = raw_input("Input number:")

    print A

    C = int(raw_input("Continue? Enter 1 to continue, anything else to stop"))

    if C == 1:

        x = 0

    else:

        x = 1
        print "mmkaybaiiiii"
