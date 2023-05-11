# https://www.acmicpc.net/problem/11653

from sys import stdin

n = int(stdin.readline())
answer = []
i = 2
while (i*i <= n):
    while True:
        div, mod = divmod(n, i)
        if mod == 0:
            answer.append(i)
            n = div
        else:
            break
    i += 1
if n != 1:
    answer.append(n)
print(*answer)
