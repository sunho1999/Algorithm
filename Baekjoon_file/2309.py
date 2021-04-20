list = []

for i in range(9):
    list.append(int(input()))

list.sort()
sum = sum(list)
for i in range(9):
    for j in range(i+1,9):
        if sum - (list[i]+list[j]) == 100:
            a = list[i]
            b = list[j]
list.remove(a)
list.remove(b)


for i in list:
    print(i)
