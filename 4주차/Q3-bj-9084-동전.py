# https://www.acmicpc.net/problem/9084

import sys

T = int(sys.stdin.readline())

'''
1
2
1 2
1000
'''

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

fib = {}
# 1, 2원으로 1000원을 만드는 경우의 수
for k in range(1, M+1):
    if k == 1:
        f = 1
    elif k == 2:
        f = 2
    else:
        if k % 2 == 0:
            f = fib[k-coins[0]] + 1 
        else:
            f = fib[k-coins[0]]
    fib[k] = f

print(fib[M])






