# https://www.acmicpc.net/problem/6064

from sys import stdin
import math

def solution():
    m, n, x, y = map(int, stdin.readline().split())
    lcm = math.lcm(m, n)
    for i in range(x, lcm + 1, m):
        num = (i - y) / n
        if num.is_integer():
            return i
    return -1
            

answer = []
for _ in range(int(stdin.readline())):
    answer.append(solution())

print(*answer)

"""
1 ≤ M, N ≤ 40000, 
1 ≤ x ≤ M, 
1 ≤ y ≤ N

연립합동방정식 
"""


