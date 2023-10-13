first= int(raw_input("Enter first time value:"))
second= int(raw_input("Enter Second time value:"))
if (first<10):
    first = first%1
elif (first>10) and (first<100):
    first = first%10
print first ,second
