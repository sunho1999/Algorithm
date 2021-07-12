import sys

n, m = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
check = [0 for _ in range(n)]
answer = []


def back(index, n, m):
    if index == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(n):
        if not check[i]:
            check[i] = 1
            answer.append(num_list[i])
            back(index + 1, n, m)
            answer.pop()
            check[i] = 0


back(0, n, m)