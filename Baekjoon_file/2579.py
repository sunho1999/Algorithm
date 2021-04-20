test_case = int(input())
s_list = [0 for i in range(300)]
dp=[0 for j in range(300)]
for i in range(test_case):
    s_list[i] = (int(input()))

dp[0] = s_list[0]
dp[1] = s_list[0]+s_list[1]
dp[2] = max(s_list[1]+s_list[2], s_list[0]+s_list[2])
for i in range(3,test_case):
    dp[i] = max(dp[i-3]+s_list[i-1]+s_list[i], dp[i-2]+s_list[i])
print(dp[test_case-1])