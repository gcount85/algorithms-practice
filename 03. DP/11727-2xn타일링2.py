from sys import stdin


def solution(n):
    if n in memo:
        return memo[n]
    memo[n] = (solution(n-1) + solution(n-2) * 2) % 10007
    return memo[n]


n = int(stdin.readline())
memo = {1: 1, 2: 3, 3: 5}
print(solution(n))

"""
- 2xn 타일을 만드는 방법
    1. 2x(n-1) 타일에 2x1 타일을 붙이는 방법
    2. 2x(n-2) 타일에 1x2 타일 두개, 2x2 타일 하나를 붙이는 방법 

"""