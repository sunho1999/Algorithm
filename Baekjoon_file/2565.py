n = int(input())
line1 = []
max_num = 0
for i in range(n):
    a,b = map(int,input().split())
    line1.append((a,b))

line1.sort()
continue_list = [j for i,j in line1]

dp = [0 for _ in range(len(continue_list))]
max_num = 0
max_cnt = 0
for i in range(len(continue_list)):
    for j in range(i):
        if continue_list[i] > continue_list[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] +=1
max_num = max(dp)
answer = n-max_num


print(answer)

