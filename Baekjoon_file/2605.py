
# 문제 접근

# 해당 학생들이 왼쪽으로 줄을 서는데 반대로 생각하여 오른쪽으로 줄을 세우고 반대부터 탐색하여 출력한다. python list 특성상 값을 추가 할 때마다 오른쪽으로 추가되기 때문이다.


n = int(input())

test_case = list(map(int,input().split())) # 테스트 케이스 입력 받는 list
answer = []




cnt = 1 # 학생 넘버수
for i in test_case:
    answer.insert(i,cnt)
    cnt +=1

for i in range(n-1,-1,-1):
    print(answer[i], end = " ")
