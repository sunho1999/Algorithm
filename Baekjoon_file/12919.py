import sys
original_text = list(input())
target_text = list(input())

def check(t): # 문자열 T 리스트를 입력받아
    if t==original_text:
        print(1)
        sys.exit()
    if len(t)==0:
        return 0
    if t[-1]=='A': # 마지막이 A이면
        check(t[:-1]) # 제거해서 재귀
    if t[0]=='B': # 처음이 B이면
        check(t[1:][::-1]) # B제거하고, 뒤집어서 재귀
check(target_text)
print(0)