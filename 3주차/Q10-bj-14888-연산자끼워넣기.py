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
최대 = -1000000000

def dfs_visit(idx: int, i: tuple):        # i = ('+', '/', '*', '-', '+')
    global tmp_max, tmp_min, A
    if idx == N-1:
        return
    else:
        if idx == 0:
            tmp_min = eval(i[idx].join([str(A[idx]), str(A[idx+1])]))
            tmp_max = eval(i[idx].join([str(A[idx]), str(A[idx+1])]))
        else:
            if i[idx] == '//':
                if tmp_max < 0:
                    tmp_max = -eval(i[idx].join([str(-tmp_max), str(A[idx+1])]))
                    tmp_min = eval(i[idx].join([str(tmp_min), str(A[idx+1])]))
                if tmp_min < 0:
                    tmp_min = -eval(i[idx].join([str(-tmp_min), str(A[idx+1])]))
                    tmp_max = eval(i[idx].join([str(tmp_max), str(A[idx+1])]))
                else:
                    tmp_min = eval(i[idx].join([str(tmp_min), str(A[idx+1])]))
                    tmp_max = eval(i[idx].join([str(tmp_max), str(A[idx+1])]))
            else:
                tmp_min = eval(i[idx].join([str(tmp_min), str(A[idx+1])]))
                tmp_max = eval(i[idx].join([str(tmp_max), str(A[idx+1])]))
        dfs_visit(idx+1, i)

for i in 연산자순열:
    tmp_min = 0
    tmp_max = 0
    idx = 0
    dfs_visit(idx, i)
    if tmp_min < 최소:
        최소 = tmp_min
    if tmp_max > 최대:
        최대 = tmp_max

print(최대)
print(최소)


