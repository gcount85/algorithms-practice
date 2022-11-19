
# memoization & 재귀 이용하기

memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    memo[n] = f
    return f


# 반복문을 이용하는 방법(상향식 접근)
fib = {}
n = 90
for k in range(1, n+1):
    if k <= 2:
        f = 1
    else:
        f = fib[k-1] + fib[k-2]
    fib[k] = f
print(fib[n])
