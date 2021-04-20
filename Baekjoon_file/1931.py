import sys

test_case = int(sys.stdin.readline())
list = []
cnt = []
for i in range(test_case):
    a,b = map(int,sys.stdin.readline().split())
    list.append([a,b])

list = sorted(list,key=lambda x: (x[1],x[0]))


start_time = 0
sum = 0
for i in range(len(list)):
    if list[i][0] >= start_time:
        start_time = list[i][1]
        sum+=1
print(sum)
