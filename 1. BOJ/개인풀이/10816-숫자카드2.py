# https://www.acmicpc.net/problem/10816
from collections import Counter

import sys

# input = sys.stdin.readline
input = sys.stdin.read().splitlines()

cards = map(int, input[1].split())
guess = map(int, input[3].split())

counter = Counter(cards)
answer = [counter[g] for g in guess]

print(*answer)
