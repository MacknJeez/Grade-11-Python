n =int(raw_input("Enter number of words you want to check :"))

list1 = ['a','e','i','o','u']
c = 0
while c < n:
    a = str(raw_input("Enter:"))
    if a in list1[0:5]:
        print 'vowel'
        c +=1
    else :
        print 'Not a vowel'
