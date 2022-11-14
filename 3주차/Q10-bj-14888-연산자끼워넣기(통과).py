# https://www.acmicpc.net/problem/14888

import sys
from itertools import permutations
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
operator = list(map(int, sys.stdin.readline().strip().split()))  # + - X / → 2 1 1 1 
연산자 = ['+', '-', '*', '//']
엣지갯수 = sum(operator)
edges = [[] for _ in range(엣지갯수)]

idx = 0
for j, v in enumerate(operator):     #2, 1, 1, 1
    while v != 0:
        edges[idx] = 연산자[j]
        v -= 1
        idx += 1

연산자순열 = set(list(permutations(edges)))
최소 = 1000000000
최대 = -100000000

def dfs_visit(idx: int, i: tuple):        # i = ('+', '/', '*', '-', '+')
    global tmp, A
    if idx == N-1:
        return
    else:
        if idx == 0:
            if i[idx] == '+':
                tmp = A[idx] + A[idx+1]
            if i[idx] == '//':
                tmp = A[idx] // A[idx+1]
            if i[idx] == '*':
                tmp = A[idx] * A[idx+1]
            if i[idx] == '-':
                tmp = A[idx] - A[idx+1]
        else:
            if i[idx] == '//' and tmp < 0:
                tmp = (-tmp // A[idx+1]) * -1
            else:
                if i[idx] == '+':
                    tmp += A[idx+1]
                if i[idx] == '//':
                    tmp //= A[idx+1]
                if i[idx] == '*':
                    tmp *= A[idx+1]
                if i[idx] == '-':
                    tmp -= A[idx+1]
        dfs_visit(idx+1, i)

for i in 연산자순열:
    tmp = 0
    idx = 0
    dfs_visit(idx, i)
    if tmp < 최소:
        최소 = tmp
    if tmp > 최대:
        최대 = tmp

print(최대)
print(최소)


