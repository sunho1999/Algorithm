# 문제 접근

# 문자를 입력받을 때 마다 처리를 해줘야함.
import sys

testcase = int(sys.stdin.readline())

for i in range(testcase):
    answer = []
    check = []
    text = sys.stdin.readline().rstrip()
    for j in text:
        if j == '<':
            if answer : # answer에 값이 있을 때 < 를 만나면 <로 갈때 지나치는 문자를 check로 저장해놈.
                check.append(answer.pop())
        elif j == '>': # check에 값이 있을 때 > 를 만나면 기존 저장해놨던 check에서 문자를 뽑아서 붙임.
            if check:
                answer.append(check.pop())
        elif j == '-': # -를 만나면 그냥 뻄
            if answer:
                answer.pop()
        else:
            answer.append(j)

    check.reverse()
    answer = answer + check

    a = "".join(answer)
    print(a)



