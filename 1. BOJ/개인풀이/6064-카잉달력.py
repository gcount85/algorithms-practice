from sys import stdin

def solution():
    m, n, x, y = map(int, stdin.readline().split())
    for i in range(40000):
        num = ((m * i) - (y - x)) / n
        if num.is_integer():
            # print(num)
            return i * m + x
    return -1
            

answer = []
for _ in range(int(stdin.readline())):
    answer.append(solution())

print(*answer)

"""
1 ≤ M, N ≤ 40000, 
1 ≤ x ≤ M, 
1 ≤ y ≤ N
"""


