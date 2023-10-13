#Program to find area OR perimeter of a circle depending on user input - Uncle Sam

#Explains to the user what to do
print "I calculate the area or perimeter of a circle depending on your input"

choose = int(raw_input("Input 1 for area, 2 for perimeter:"))
R = int(raw_input("Enter the radius of the circle:"))

#Defines area and perimeter variables
A = 3.14 * (R**2)
P = 2 * 3.14 * R

if choose == 1:
    print "The area is", A, "square units"
elif choose == 2:
    print "The perimeter is", P, "units"
else:
    print "Choose 1 or 2 bro!"
