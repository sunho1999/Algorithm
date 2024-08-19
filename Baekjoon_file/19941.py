n, k = map(int, input().split())

st = list(input())

# 햄버거를 먹을 수 있는 사람의 수
count = 0

if n < k:
    k = n
for i in range(n):
    if st[i] == 'P':
        for j in range(i-k,i+k+1):
            if j >= n:
                break
            elif j < 0:
                continue
            if st[j] == 'H':
                count += 1
                st[j] = 'X'
                break

print(count)