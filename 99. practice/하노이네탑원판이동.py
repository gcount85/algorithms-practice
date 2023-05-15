from sys import stdin, setrecursionlimit

setrecursionlimit(10**4)

def move(n, a, b, c):
    global count
    if n == 1:
        count += 1
        return
    move(n-2, a, c, b)
    move(1, a, (c+b)//2, b)
    move(1, a, b, c)
    move(1, (c+b)//2, b, a)
    move(n-2, c, b, a)

n = int(stdin.readline())
count = 0
move(n, 1, 4, 2)  # n, count, 출발지탑, 목적지탑, 보조탑
print(count)
