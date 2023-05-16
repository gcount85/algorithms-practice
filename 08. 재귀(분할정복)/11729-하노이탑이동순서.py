from sys import stdin

n = int(stdin.readline())


def hanoi(n, a, b, c):
    if n == 1:
        print(a, b)
        return
    hanoi(n-1, a, c, b)
    hanoi(1, a, b, c)
    hanoi(n-1, c, b, a)

print(2**n-1) # 하노이탑 이동 횟수
hanoi(n, 1, 3, 2) # 출발판, 목적지판, 보조판 
