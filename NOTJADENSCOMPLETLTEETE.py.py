import time
l=[]
for i in range(1000,3001):
    l.append(str(i))
for i in range(0,len(l)):
    flag=0

    for j in range(0,4):
        time.sleep(0.15)
        if int(l[i][j])%2==0:
           flag=1
        else:
            flag=0
            break
    if flag==1:
        print l[i],",",
