import sys

(sorted_num := [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]).sort()
for i in sorted_num:
    print(i)

# 수 정렬하기1과 동일한 알고리즘으로 했는데 성공함