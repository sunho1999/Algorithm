n,m = map(int,input().split())

num_list = list(map(int,input().split())) # -7,-3,-2,5,8

cnt = 0
for i in range(n-1):
    dp = [0 for _ in range(n)]
    dp[i] = num_list[i]
    for j in range(i+1,n):
        dp[j] = dp[j-1] + num_list[j]
    if m in dp[i:]:
        cnt +=1
    print(dp)
print(cnt)
