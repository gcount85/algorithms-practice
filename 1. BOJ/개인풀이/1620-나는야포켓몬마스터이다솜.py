import sys

input = sys.stdin.readline
N, M = map(int, input().split())
dict = {}
dict2 = {}
for i in range(1, N+1):
    item = input().strip()
    dict[i] = item
    dict2[item] = i

for _ in range(M):
    guess = input().strip()
    if guess.isdigit():
        print(dict[int(guess)])
    else:
        print(dict2[guess])
