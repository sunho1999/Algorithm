N = int(input())

M = int(input())

remote = {str(i) for i in range(10)}
if M > 0:
    remote -= set(map(str,input().split()))
result = 0
#case 1
min_cnt = abs(100-N)

#case 2

for i in range(1000001):
    for j in range(len(str(i))):
        if str(i)[j] not in remote:
            break
        elif len(str(i)) -1 == j:
            min_cnt = min(min_cnt,abs(i-N)+len(str(i)))

print(min_cnt)

