""" n=int(input())
n0=0
n1=1
f=0
count=0

for i in range(n-1):
    f=n0+n1
    n0=n1
    n1=f
    for j in range(1,f+1):
        if f%j==0:
            count+=1
    if count > 2:
        for j in range(f-1,1,-1):
            if f%j==0:
                disor=j
                break
    else:
        disor=1
            
print('f(%d) = %d'%(n,f))
print('Biggest Disor = %d'%disor) """
#####################################################
""" import sys
input = sys.stdin.readline

n = int(input())
total = 0
if n<10:
    for i in range(1,n+1):
        if i % 2 == 0:
            total += i
else:
    m = n%10*10+n//10
    print(m)
    for i in range(1,m+1):
        if i % 2 == 0:
            total += i
print("Total =",total) """
#########################################################

