from itertools import permutations
import sys


# N = int(sys.stdin.readline())
# 비용 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# N = 4
# 비용 = [
#     [0, 10, 15, 20],
#     [5, 0, 9, 10],
#     [6, 13, 0, 12],
#     [8, 8, 9, 0],
# ]
N = 3
비용 = [
    [0, 0, 10],
    [5, 0, 2],
    [0, 3, 0],
]
# print(비용)

도시목록 = range(N)
도시목록순열 = []  # 마지막에 첫번째 수를 다시 추가해야 함! 
# print(도시목록순열)

# 방문할 수 없는 도시들의 인덱스 모음
인덱스 = []
for i, v in enumerate(비용):
    print(i, v)
    if v.count(0) > 1:
        for j, k in enumerate(v):
            if j != i and k == 0:   
                인덱스.append((i, j))
print(인덱스)

# 방문할 수 없는 도시들의 인덱스를 참조하여 유효하지 않은 순열 제거
for c in permutations(도시목록):       # 0, 2, 1
    for i in 인덱스:         # 0, 1
        for n in range(N):   # 0, 1, 2
            # print(i)
            if n == N-1:
                if c[N-1]+c[0] != i:
                    도시목록순열.append(c)
            else:
                if c[n:n+2] != i:
                    도시목록순열.append(c)
print(도시목록순열)

# 순열의 비용을 재귀적으로 구하는 함수~~ 
# def 비용더하기(i, 순열):
#     # (0, 3, 2, 1)
#     if i == N-1:  #인덱스가 3 
#         return 비용[순열[i]][순열[0]] 
#     else:
#         return 비용[순열[i]][순열[i+1]] + 비용더하기(i+1, 순열)

# 비용합목록 = [비용더하기(0, i) for i in 도시목록순열]

# print(min(비용합목록))



