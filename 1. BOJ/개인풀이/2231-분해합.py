import sys


def solution():
    input = sys.stdin.readline

    N = int(input())

    for i in range(N):
        if i + sum(int(digit) for digit in str(i)) == N:
            return i
    return 0


print(solution())
