from operator import itemgetter
num= int(input())

age_list = []

for i in range(num):
    age_list.append(list(input().split()))

for i in range(len(age_list)):
    age_list[i][0] = int(age_list[i][0])

age_list.sort(key=itemgetter(0),reverse=False)


for i in range(len(age_list)):
    print(str(age_list[i][0])+" "+age_list[i][1])