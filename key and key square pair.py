
#WAP to have key:key^2 pair

a = raw_input("Do you want to ?[Yeet/Nein]:")
while (a == "Yeet") or (a=="yeet"):
        len_dict1 = int(raw_input("Enter length of dictionary:"))
        dict1 = {}
    for i in range(1,len_dict1+1):
        dict1[i] = i**2
    print dict1
else:
        print"Not valid input"
        a =raw_input("Have you changed your mind ?:")
