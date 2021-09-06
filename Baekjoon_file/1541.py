a = input().split('-')
num = []
# - 기준으로 나뉜 숫자들 탐색
for i in a:
    cnt = 0
    s = i.split('+') # + 가 있다면 그 인덱스 값 분해 후 분해한 값들 각각 더해서 리스트에 추가

    for j in s:
        cnt += int(j)
    num.append(cnt)

n = num[0]
for i in range(1, len(num)): # 다 계산된 숫자를 빼기
    n -= num[i]
print(n)
