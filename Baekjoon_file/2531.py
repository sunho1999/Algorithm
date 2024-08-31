from collections import defaultdict

n,d,k,c = map(int,input().split())

sushi_list = []
for i in range(n):
    sushi_list.append(int(input()))

sushi_list = sushi_list + sushi_list[:k-1]

max_sushi = 0
left , right = 0, 0
window = defaultdict(int)
window[c] +=1
while right < k:  #처음 k개로 초기값 만들기
    window[sushi_list[right]] +=1
    right+=1

for _ in range(n-1):
    max_sushi = max(max_sushi, len(window))
    window[sushi_list[right]] +=1
    window[sushi_list[left]] -=1
    if window[sushi_list[left]] == 0:
        window.pop(sushi_list[left])
    right+=1
    left+=1
print(max_sushi)