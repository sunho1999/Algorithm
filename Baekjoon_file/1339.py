n = int(input())

alph_list = []
dic = {}

for i in range(n):
    a = input()
    alph_list.append(a)

for word in alph_list:
    k = len(word)-1
    #알파벳 분해하면서 10^자리수
    for s in word:
        if s in dic:
            dic[s] += 10**k
        else:
            dic[s] = 10**k
        k = k-1
#숫자 담을 리스트
num_list = []
for value in dic.values():
    num_list.append(value)

num_list.sort(reverse=True)

answer = 0
max = 9
for i in range(len(num_list)):
    answer = answer + num_list[i] * max
    max -=1
print(answer)