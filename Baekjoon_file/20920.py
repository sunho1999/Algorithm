# 다음과 같은 우선순위를 차례로 적용하여 만들어진다.
#
# 자주 나오는 단어일수록 앞에 배치한다.
# 해당 단어의 길이가 길수록 앞에 배치한다.
# 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
#
# M보다 짧은 길이의 단어의 경우 읽는 것만으로도 외울 수 있기 때문에 길이가 M이상인 단어들만 외운다고 한다.

import sys
from collections import defaultdict
input = sys.stdin.readline

n,m = map(int,input().split())
word_list = defaultdict(int)
for i in range(n):
    word = input().strip()
    if len(word) >= m:
        word_list[word] +=1
sort_dict = sorted(word_list.items() ,key =lambda x : (-x[1],-len(x[0]),x[0]))


for i in sort_dict:
    print(i[0])