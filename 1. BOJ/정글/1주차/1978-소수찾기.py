import sys

개수 = int(input())
숫자리스트 = list(map(int, sys.stdin.readline().split()))
c = 0
for i in 숫자리스트:
    if i != 1:
        약수개수 = len([n for n in range(2, i) if i % n == 0])
        if 약수개수 == 0:
            c += 1
print(c)

