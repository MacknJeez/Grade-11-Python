
l1 = [0,2,4,6,8]
l2 = [2,4,6,8]
for i in range(1000,3001):
    if i % 10 in l1 :
        x= i%10
        if x in l1 :
            y= i%10
            if y in l1:
                z= i%10
                if z in l1:
                    print i
