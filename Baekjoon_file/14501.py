n = int(input())
consult_list = [0 for _ in range(n)]
dp = [0 for _ in range(n+1)]
for i in range(n):
    T,P = map(int,input().split())
    consult_list[i] = [T,P]

max_sum = 0
for i in range(n): # 7번 반복
    for j in range(i+consult_list[i][0],n+1):
        if dp[j] < dp[i] + consult_list[i][1]:
            dp[j] = dp[i] + consult_list[i][1]

print(dp[-1])
