import sys

input = sys.stdin.readline
str = input().rstrip()
bomb = list(input().rstrip())

m = len(bomb)
answer = []
for i in str:
    # answer에 넣기
    answer.append(i)
    # 폭탄 끝과 현재 인덱스 끝이 일치하고
    if i == bomb[-1]:
        # 폭발문자열과 일치할 경우
        if answer[-m:] == bomb:
            del answer[-m:]

if answer:
    result = "".join(answer)
    print(result)


else:
    print("FRULA")