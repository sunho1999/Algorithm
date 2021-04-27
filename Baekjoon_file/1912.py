n = int(input())

test_case = list(map(int,input().split()))

sum = [test_case[0]]
for i in range(n-1):
    sum.append(max(sum[i]+test_case[i+1] , test_case[i+1]))

print(max(sum))

