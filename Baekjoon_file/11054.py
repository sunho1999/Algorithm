n = int(input())

num_list = list(map(int, input().split()))
reverse_list = num_list[::-1]

increase = [1 for _ in range(n)] # 가장 긴 증가하는 부분 수열
decrease = [1 for _ in range(n)] # 가장 긴 감소하는 부분 수열

for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_list[i] > reverse_list[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for _ in range(n)]
for i in range(n):
    result[i] = increase[i] + decrease[n-i-1] -1

print(max(result))