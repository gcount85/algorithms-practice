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
    # if i % 3 == 0:
    #     memo[i] = memo[i/3] + 1

    # elif i % 2 == 0:
    #     memo[i] = memo[i/2] + 1

    # else:  # 1을 뺀다
    #     memo[i] = memo[i-1] + 1

    memo[i] = min(memo[i/3] if i/3 in memo else maxnum, memo[i/2] if i /
                  2 in memo else maxnum, memo[i-1] if i-1 in memo else maxnum) + 1


print(memo[n])
