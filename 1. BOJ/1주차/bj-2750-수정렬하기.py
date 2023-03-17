import sys

(sorted_num := [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]).sort()
for i in sorted_num:
    print(i)

