#Program to calculate the grade given a mark

M = int(raw_input("Enter marks:"))

if 91 <= M and  M <= 100:
    grade = "A1"

elif 81 <= M and M <= 90:
    grade = "A2"

elif 71 <= M and M <= 80:
    grade = "B1"

elif 61 <= M and M <= 70:
    grade = "B2"

elif 41 <= M and M <= 60:
    grade = "C"

elif 0 <= M and M <= 40:
    grade = "F"

print "Your grade is", grade
