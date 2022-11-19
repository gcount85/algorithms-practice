import sys

n = int(sys.stdin.readline())

fib = {}
for k in range(1, n+1):
    if k == 1:
        f = 1
    elif k == 2:
        f = 2
    else:
        f = (fib[k-1] + fib[k-2]) % 15746  # 마지막에 나누지 말고 바로 나눠주어야 효율적 → 아니면 시간 초과 뜨기 십상
        del fib[k-2]   # 필요없는 키 지워야 효율적
    fib[k] = f

print(fib[n])