
import sys

n = int(sys.stdin.readline())

fib = {}
for k in range(1, n+1):
    if k == 1:
        f = 1
    elif k == 2:
        f = 2
    else:
        f = fib[k-1] + fib[k-2]
    fib[k] = f
print(fib[n]%15746)