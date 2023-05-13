# https://www.acmicpc.net/problem/8611

import sys


def to_n_base(num, base):
    result = []
    while num:
        num, remainder = divmod(num, base)
        result.append(str(remainder))
    return ''.join(reversed(result))


input = sys.stdin.readline
str_n = input().strip()  # 스트링 숫자 15
answer = []

for i in range(2, 11):
    converted_num = to_n_base(int(str_n), i)
    length = len(converted_num)

    s, e = 0, length-1
    isPalindrome = 1

    while s < e:
        if converted_num[s] != converted_num[e]:
            isPalindrome = 0
            break
        s += 1
        e -= 1

    if isPalindrome == 1:
        answer.extend([i, converted_num])

print(*answer if answer else ["NIE"])
