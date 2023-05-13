import sys


def dp(k, n, dp_table):
    for floor in range(k+1):
        for room in range(1, n+1):
            if floor == 0:
                dp_table[0][room] = room
            elif room == 1:
                dp_table[floor][1] = 1
            else:
                dp_table[floor][room] = dp_table[floor][room-1] + \
                    dp_table[floor-1][room]


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    dp_table = [[0] * (n+1) for _ in range(k+1)]

    dp(k, n, dp_table)
    # print(dp_table)
    print(dp_table[k][n])
