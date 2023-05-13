import sys

n = int(sys.stdin.readline())

fib = {}
for k in range(1, n+1):
    if k <= 3:
        f = 1
    else:
        f = fib[k-1] + fib[k-3]
    fib[k] = f
print(fib[n])