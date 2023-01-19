# https://www.acmicpc.net/problem/9663
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제

import sys
input = sys.stdin.readline

n = int(input())
count = 0
row = set()
pos_diag = set()
neg_diag = set()
dp = [0] * n


def dfs(x):
    global row, pos_diag, neg_diag, count
    if x == n:
        count += 1
        return
    for i in range(n):
        if i in row:
            continue
        if i-x in pos_diag:
            continue
        if i+x in neg_diag:
            continue
        dp[x] = i
        # set에 불가능한 자리의 경우의 수를 추가
        row.add(i)
        pos_diag.add(i-x)
        neg_diag.add(i+x)
        dfs(x + 1)
        # 리턴하면서 원소 제거
        row.remove(i)
        pos_diag.remove(i-x)
        neg_diag.remove(i+x)


dfs(0)
print(count)
