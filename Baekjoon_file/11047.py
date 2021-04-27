n , goal = map(int,input().split())
coin_list =[]
sum = 0
#동전 저장
for i in range(n):
    coin_list.append(int(input()))
max = 0

for i in range(n-1,-1,-1):
    if coin_list[i] > goal:
        continue
    else:
        sum = sum + goal//coin_list[i]
        goal = goal%coin_list[i]
print(sum)