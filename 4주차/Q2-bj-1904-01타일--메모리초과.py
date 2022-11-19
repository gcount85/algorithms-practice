
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
        del fib[k-2]   # 필요없는 키 지움 
    fib[k] = f

print(fib)
print(fib[n]%15746)