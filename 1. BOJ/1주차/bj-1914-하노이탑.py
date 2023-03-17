import sys


def 하노이(n, a, b, c):  # 원판갯수, 시작위치, 보조, 끝위치
    if n == 1:
        print(a, c)
    else:
        하노이(n-1, c, a, b)
        하노이(1, a, b, c)
        하노이(n-1, b, a, c)


n = int(sys.stdin.readline())
print(2**n-1)
if(n <= 20):
    하노이(n, 1, 2, 3)

