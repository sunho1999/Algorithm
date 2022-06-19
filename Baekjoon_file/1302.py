# dictionary 이용

testnum = int(input()) # 갯수
testcase = []
for i in range(testnum):
    testcase.append(input())
real_answer = []
answer = {}
for i in testcase:
    if i not in answer:
        answer[i] = 0
    answer[i] +=1

max_num = max(answer.values())

for key,value in answer.items():
    if value == max_num:
        real_answer.append(key)
real_answer = sorted(real_answer,reverse=True)
print(real_answer[-1])