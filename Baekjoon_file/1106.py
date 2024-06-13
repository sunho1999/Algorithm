people,city=map(int,input().split())
data=[]
for i in range(city):
    v,p =map(int,input().split())
    data.append([v,p])

dp=[1e6]*(100+people)
dp[0]=0

for i,j in data:
    for k in range(1,100+people):
        if j<=k:
            dp[k]=min(dp[k],dp[k-j]+i)


print(min(dp[people:]))