import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001 # 10000개 들어오니까 수를 넣기 쉽게 10001의 값이 담긴 list를 만든다.

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1 # 값 들어오면 추가

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)