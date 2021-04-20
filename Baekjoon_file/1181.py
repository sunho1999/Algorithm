num = int(input())
word_list = []

for i in range(num):
    word_list.append(input())
set_word_list =list(set(word_list))
sort_list=[]
for i in set_word_list:
    sort_list.append((len(i),i))
sort_list.sort()


for i,j in sort_list:
    print(j)