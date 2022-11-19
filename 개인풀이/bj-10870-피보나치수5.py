import sys

n = int(sys.stdin.readline())

fib = {}
for k in range(n+1):
    if 0 < k < 3:
        f = 1
    elif k == 0:
        f = 0
    else:
        f = fib[k-1] + fib[k-2]
    fib[k] = f
print(fib[n])


 