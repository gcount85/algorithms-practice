import sys

"""
X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.

"""

n = int(sys.stdin.readline())
memo = {1: 0, 2: 1, 3: 1}
maxnum = 1000000
for i in range(4, n+1):
    memo[i] = min(memo.get(i//3, maxnum), memo.get(i //
                  2, maxnum), memo.get(i-1, maxnum)) + 1

print(memo[n])
