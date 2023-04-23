import sys

input = sys.stdin.readline
n = int(input())


def solution(n):
    if n < 10:
        return 1
    min_value = float('inf')
    for i in range(9, 0, -1):
        if n % i == 0:
            min_value = min(n//i, min_value)
        else:
            min_value = min((n//i) + 1, min_value)
    return min_value


print(solution(n))

"""
n이 10보다 작으면 1
10 이상이면? n//2 부터 n//9 

"""

