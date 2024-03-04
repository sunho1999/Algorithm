# 규칙
# 1.문자열의 뒤에 A를 추가한다.
# 2.문자열을 뒤집고 뒤에 B를 추가한다.
import sys

sys.setrecursionlimit(10 ** 6)
s = input()
target = input()
cnt = len(target) - len(s)


while(len(target)!= len(s)):
    if target[-1] == "A":
        target = target[:-1]
    elif target[-1] == "B":
        target = target[:-1]
        target = target[::-1]
if target == s:
    print(1)
else:
    print(0)