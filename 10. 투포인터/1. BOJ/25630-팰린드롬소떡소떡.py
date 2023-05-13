import sys

input = sys.stdin.readline
n = int(input())
string = input().strip()

count, s, e = 0, 0, n-1
while s < e:
    if string[s] != string[e]:
        count += 1
    s += 1
    e -= 1

print(count)
