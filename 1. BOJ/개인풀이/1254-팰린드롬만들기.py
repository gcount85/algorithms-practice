# https://www.acmicpc.net/problem/1254
# refactored

import sys

input = sys.stdin.readline
string = input().strip()

n = len(string)
temp_str = ""
string_copy = string


def is_palindrome(s):
    return s == s[::-1]


for i in range(n):
    if not is_palindrome(string_copy):
        temp_str = string[i] + temp_str
        string_copy = string + temp_str
    else:
        break

print(n + i)
