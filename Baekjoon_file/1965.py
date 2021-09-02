n = int(input())
box_list = list(map(int, input().split()))
dp = []
dp.append(1)
for i in range(1, n):
    d = []
    for j in range(i):
        if box_list[i] > box_list[j]:
            d.append(dp[j] + 1)
    if not d:
        dp.append(1)
    else:
        dp.append(max(d))
print(max(dp))