# https://www.acmicpc.net/problem/1541

# 나의 버전

import sys

input = sys.stdin.readline().rstrip().split("-")

# print(input)
if len(input) == 1:
    ans = sum(list(map(int, input[0].split("+"))))
    del input[0]
else:    # 뺄셈이 한개 이상 존재
    a = sum(list(map(int, input[0].split("+"))))
    b = sum(list(map(int, input[1].split("+"))))
    ans = a - b
    del input[0]
    del input[0]

while len(input) != 0:
    a = sum(list(map(int, input[0].split("+"))))
    ans -= a
    del input[0]
         
print(ans)


# 버전 2

import sys

input = sys.stdin.readline().rstrip().split("-")
ans = 0

for i in input[0].split("+"):
    ans += int(i)

for i in input[1:]:
    for j in i.split("+"):
        ans -= int(j)

         
print(ans)

