
import sys

input = sys.stdin.readline
N = int(input())
count = 0
i = 666

while True:
    if '666' in str(i):
        count += 1
    if count == N:
        print(i)
        break
    i += 1
