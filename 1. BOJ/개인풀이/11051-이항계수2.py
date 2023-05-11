# https://www.acmicpc.net/problem/11051

from sys import stdin, setrecursionlimit

setrecursionlimit(10**3)

memo = {(1,0) : 1, (1,1) : 1, (0,0) : 1}
def biCo(n, k):
    if k == 0 or n == k:
        return 1
    if (n,k) in memo:
        return memo[(n,k)]
    memo[(n,k)] = (biCo(n-1, k-1) + biCo(n-1, k)) % 10007 
    return memo[(n,k)]

n, k = map(int, stdin.readline().strip().split())
print(biCo(n, k))


"""
- 파스칼의 삼각형 이용
dp(1,0) = dp(1,1) = dp(0,0) = dp(n,0) = dp(n,n) = 1

dp(n,k) = dp(n-1, k-1) + dp(n-1, k)

"""
