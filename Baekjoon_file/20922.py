from collections import defaultdict
import sys
input= sys.stdin.readline
n,k = map(int,input().split())
li = list(map(int,input().split()))
left, right = 0, 0
dd = defaultdict(int)
ans = 0

while True:
    if right == n:
        break
    if dd[li[right]] < k:
        dd[li[right]] +=1
        right +=1
    else:
        dd[li[left]] -=1
        left +=1
    ans = max(right - left, ans)
print(ans)