import sys

a, b = sys.stdin.readline().split()
a = int(a)
b = int(b)
poc_list = []
poc_list.append("@")
dic= {}
for i in range(1,a+1):
    a = sys.stdin.readline().rstrip()
    poc_list.append(a)
    dic[a] = i


for j in range(b):
    q = sys.stdin.readline().rstrip()
    if q.isalpha():
        print(dic[q])
    if q.isdigit():
        print(poc_list[int(q)])



