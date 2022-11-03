from itertools import permutations
import sys


N = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# N = 4
# 비용 = [
#     [0, 10, 15, 20],
#     [5, 0, 9, 10],
#     [6, 13, 0, 12],
#     [8, 8, 9, 0],
# ]
# N = 3
# cost = [
#     [0, 0, 10],
#     [5, 0, 2],
#     [0, 3, 0],
# ]

city_list = range(N)
city_perm = list(permutations(city_list))  # 마지막에 첫번째 수를 다시 추가해야 함! 
# print(city_perm)

# 방문할 수 없는 도시들의 인덱스 모음
# 리스트컴프리헨션
index = [(i, j) for i, v in enumerate(cost) if v.count(0) > 1 for j, k in enumerate(v) if j != 1 and k == 0]

# 그냥 for append
# 인덱스 = []
# for i, v in enumerate(비용):
#     # print(i, v)
#     if v.count(0) > 1:
#         for j, k in enumerate(v):
#             if j != i and k == 0:   
#                 인덱스.append((i, j))
# print(인덱스)

# 방문할 수 없는 도시들의 인덱스를 참조하여 유효하지 않은 순열 제거
for c in permutations(city_list):       # 0, 2, 1
    for ii in index:         # 0, 1
        for n in city_list:   # 0, 1, 2
            # print(ii)
            if n == N-1:
                if ((c[N-1], c[0]) == ii) and (c in city_perm):
                    city_perm.remove(c)
            else:
                if (c[n:n+2] == ii) and (c in city_perm):
                    city_perm.remove(c)
# print(city_perm)

# 순열의 비용을 재귀적으로 구하는 함수~~ 
def add_cost(i, perm):
    # (0, 3, 2, 1)
    if i == N-1:  #인덱스가 3 
        return cost[perm[i]][perm[0]] 
    else:
        return cost[perm[i]][perm[i+1]] + add_cost(i+1, perm)

cost_sum_list = [add_cost(0, i) for i in city_perm] 

sys.stdout.write(min(cost_sum_list))



