import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().split())
alpha = sorted(list(sys.stdin.readline().split()))
VOWELS = set('aeiou')  # 모음

#조합으로 나올수 있는 경우의수 만들기
cm = list(combinations(alpha, l))
cm.sort()

for c in cm:
    #하나씩 탐색하면서 집합으로 C-VOWELS 구현
    diff = set(c).difference(VOWELS)
    # 모음이 하나라도 있으면 1< @ < l 이 나오기 떄문에 출력
    if 1 < len(diff) < l:
        print(''.join(c))
        continue

