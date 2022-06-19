from queue import PriorityQueue

testnum = int(input())

present = PriorityQueue()

test = []
for i in range(testnum):
    test = str(input()).split()

    if present.empty(): # present가 빈상태
        if test == ['0']:
            print(-1)
        else:
            for i in test[1:]:
                present.put((int(i)*-1))
    else: # present가 있는 상태
        if test == ['0']:
            print(present.get()*-1)
        else:
            for i in test[1:]:
                present.put((int(i)*-1))