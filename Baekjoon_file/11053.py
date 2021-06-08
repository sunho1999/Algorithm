n = int(input())

num_list = list(map(int,input().split()))

check_point = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j] and check_point[i] < check_point[j]:
            check_point[i] = check_point[j]
    check_point[i] = check_point[i] + 1

print(max(check_point))