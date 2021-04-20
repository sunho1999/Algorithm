n, m = map(int, input().split())
l = []
mini = []

for i in range(n):
    l.append(input())

for a in range(n-7):
    for i in range(m-7):
        count1=0
        count2=0
        for b in range(a,a+8):
            for j in range(i,i+8):
                if (b+j)%2 ==0:
                    if l[b][j] != 'W':
                        count1 +=1
                    elif l[b][j] != 'B':
                        count2 +=1
                else:
                    if l[b][j] !='B':
                        count1 +=1
                    elif l[b][j] !='W':
                        count2+=1
        mini.append(count1)
        mini.append(count2)
print(min(mini))
