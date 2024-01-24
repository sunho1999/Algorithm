# import sys
# input = sys.stdin.readline
#
# testcase = int(input().strip())
#
# for i in range(testcase):
#     a,b = map(int,input().strip().split()) # a/b
#     start_num = a/b
#     while (a != 1 and start_num >0):
#         stop_num = b//a +1
#         a = a*(stop_num) - b
#         b = b*(stop_num)
#         start_num = a / b
#     answer = b
#     print(answer)


import sys

from fractions import Fraction

T = int(sys.stdin.readline())

def henry(numer, denom):

    if numer == 1:
        # 8
        return denom
    else:
        x = (denom // numer) + 1
        step = Fraction(numer, denom) - Fraction(1, x)
        return henry(step.numerator, step.denominator)
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(henry(a, b))