num = int(input())

time = list(map(int,input().split()))

time.sort()
sum = 0

for i in range(num):
    for j in range(i+1):
        sum = sum + time[j]
print(sum)