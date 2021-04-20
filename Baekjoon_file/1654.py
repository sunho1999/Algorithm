
n, k  = map(int,input().split())
#기존 갖고 있는 리스트
state_list = []
for i in range(n):
    state_list.append(int(input()))

start,end = 1, max(state_list)

result = 0
while start <= end:
    mid = (start + end) // 2
    line = 0
    for i in state_list:
        line = line + i//mid
    if line >= k:
        start= mid+1
        result = mid
    elif line < k:
        end = mid-1
print(result)
