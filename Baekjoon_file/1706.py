# 4 5
# adaca
# da##b
# abb#b
# abbac

n,m = map(int,input().split())
word_list = []
mapp = [list(input()) for _ in range(n)]


# 행 탐색

for i in range(n):
    text = ''
    for j in range(m):
        if mapp[i][j] != '#':
            text += mapp[i][j]
        elif len(text) >= 2:
            word_list.append(text)
        elif mapp[i][j] == '#':
            text = ''
    if len(text) >= 2:
        word_list.append(text)
# 열 탐색

for i in range(m):
    text = ''
    for j in range(n):
        if mapp[j][i] != '#':
            text += mapp[j][i]
        elif len(text) >= 2:
            word_list.append(text)
        elif mapp[j][i] == '#':
            text = ''
    if len(text) >= 2:
        word_list.append(text)
# print(word_list)

word_list.sort()
print(word_list[0])