n,k = map(int,input().split())

money = []
for i in range(n):
    a = int(input())
    money.append(a)
dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in money:
    for j in range(1,k+1):
        if j - i >=0:
            dp[j] += dp[j-i]

print(dp[k])
