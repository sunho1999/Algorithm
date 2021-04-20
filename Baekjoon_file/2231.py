import sys
n = int(input())
sum = 0
check= 0

for i in range(1,n):
    sum = 0
    sum = sum + i
    i = str(i)
    for j in i:
        sum = sum + int(j)
        if sum == n:
            print(i)
            sys.exit(0)
        if int(i) + 1 == n:
            print(0)
            sys.exit(0)


