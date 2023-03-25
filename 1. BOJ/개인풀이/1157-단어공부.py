
import sys
from collections import Counter

input = sys.stdin.readline().lower().strip()

if (len(input) == 1):
    print(input[0].upper())
else:
    c = list(Counter(input).items())
    c.sort(key=lambda x: (-x[1]))
    if (c[0][1] == c[1][1]):
        print("?")
    else:
        print(c[0][0].upper())
