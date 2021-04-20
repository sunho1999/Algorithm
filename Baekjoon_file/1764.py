a, b = map(int,input().split())
a_list = []
b_list =[]
for _ in range(a):
    a_list.append(input())

for _ in range(b):
    b_list.append(input())

same = list(set(a_list)&set(b_list))


same.sort()
print(len(same))
for i in same:
    print(i)